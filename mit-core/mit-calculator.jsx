import { useState, useMemo, useEffect, useRef } from "react";

const OMEGA_LAMBDA = 3.52e122;
const OMEGA_H = 3.13e122;
const SQRT_OMEGA_LAMBDA = Math.sqrt(OMEGA_LAMBDA);
const SQRT_OMEGA_H = Math.sqrt(OMEGA_H);

const C = (theta) => 2 * Math.sin(Math.PI * theta) ** 2;
const logSlope = (theta) => 2 * Math.PI / Math.tan(Math.PI * theta);

const WELLS = [
  { label: "α", Fn: "F₇", pos: "13/60", theta: 13/60, grid: "60R", n: 1/30, omega: "Ω_Λ", AP: "1", obs: "Fine structure constant" },
  { label: "a₀", Fn: "F₇", pos: "13/120", theta: 13/120, grid: "120", n: 1, omega: "Ω_H", AP: "aP", obs: "MOND acceleration" },
  { label: "H₀", Fn: "F₉", pos: "34/120", theta: 34/120, grid: "120", n: 1, omega: "Ω_H", AP: "tP⁻¹", obs: "Hubble parameter" },
  { label: "Λ", Fn: "—", pos: "60/120", theta: 60/120, grid: "120", n: 2, omega: "Ω_Λ", AP: "ℓP⁻²", obs: "Cosmological constant" },
];

const SCORECARD = [
  { obs: "α", predicted: "0.00733", observed: "0.007297", agr: "~0.5%" },
  { obs: "a₀/(cH₀)", predicted: "0.184", observed: "0.183", agr: "<1%" },
  { obs: "H₀ local shift", predicted: "8.4%", observed: "~8.7%", agr: "<1%" },
  { obs: "Λ·ℓP²", predicted: "3.0×10⁻¹²²", observed: "2.84×10⁻¹²²", agr: "~5%" },
  { obs: "CMB suppression", predicted: "ℓ ~ 31", observed: "ℓ < 30", agr: "~" },
  { obs: "CMB parity", predicted: "R_TT < 1", observed: "R_TT ≈ 0.81", agr: "✓" },
  { obs: "CMB alignment", predicted: "~13°", observed: "~10°", agr: "~" },
];

const FIBONACCI = [1,1,2,3,5,8,13,21,34,55,89];

function formatSci(val) {
  if (val === 0) return "0";
  if (Math.abs(val) >= 0.001 && Math.abs(val) < 10000) return val.toPrecision(4);
  const exp = Math.floor(Math.log10(Math.abs(val)));
  const mantissa = val / Math.pow(10, exp);
  return `${mantissa.toFixed(3)} × 10^${exp}`;
}

function WaveCanvas({ width = 600, height = 200 }) {
  const canvasRef = useRef(null);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const dpr = window.devicePixelRatio || 1;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, width, height);

    const pad = { l: 50, r: 20, t: 20, b: 35 };
    const w = width - pad.l - pad.r;
    const h = height - pad.t - pad.b;
    const midY = pad.t + h / 2;

    // grid
    ctx.strokeStyle = "rgba(120,160,200,0.12)";
    ctx.lineWidth = 0.5;
    for (let i = 0; i <= 4; i++) {
      const x = pad.l + (i / 4) * w;
      ctx.beginPath(); ctx.moveTo(x, pad.t); ctx.lineTo(x, pad.t + h); ctx.stroke();
    }
    ctx.beginPath(); ctx.moveTo(pad.l, midY); ctx.lineTo(pad.l + w, midY); ctx.stroke();

    // wave
    ctx.strokeStyle = "#6ec1e4";
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let i = 0; i <= w; i++) {
      const t = (i / w) * 4 * Math.PI;
      const y = midY - Math.cos(t / 2) * (h * 0.42);
      i === 0 ? ctx.moveTo(pad.l + i, y) : ctx.lineTo(pad.l + i, y);
    }
    ctx.stroke();

    // present epoch marker
    const tNow = 5.22;
    const xNow = pad.l + (tNow / (4 * Math.PI)) * w;
    const yNow = midY - Math.cos(tNow / 2) * (h * 0.42);
    ctx.fillStyle = "#f0c040";
    ctx.beginPath(); ctx.arc(xNow, yNow, 5, 0, 2 * Math.PI); ctx.fill();
    ctx.fillStyle = "rgba(240,192,64,0.85)";
    ctx.font = "11px 'IBM Plex Mono', monospace";
    ctx.fillText("t ≈ 5.22", xNow + 8, yNow - 6);

    // axis labels
    ctx.fillStyle = "rgba(180,200,220,0.7)";
    ctx.font = "10px 'IBM Plex Mono', monospace";
    ctx.textAlign = "center";
    ["0", "π", "2π", "3π", "4π"].forEach((label, i) => {
      ctx.fillText(label, pad.l + (i / 4) * w, pad.t + h + 16);
    });
    ctx.textAlign = "right";
    ctx.fillText("+1", pad.l - 6, pad.t + 12);
    ctx.fillText("−1", pad.l - 6, pad.t + h);
    ctx.fillText("Ψ", pad.l - 6, midY + 4);
  }, [width, height]);

  return <canvas ref={canvasRef} style={{ width, height, display: "block" }} />;
}

function DomainCanvas({ width = 600, height = 180, highlightTheta = null }) {
  const canvasRef = useRef(null);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const dpr = window.devicePixelRatio || 1;
    canvas.width = width * dpr;
    canvas.height = height * dpr;
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, width, height);

    const pad = { l: 50, r: 20, t: 30, b: 40 };
    const w = width - pad.l - pad.r;
    const h = height - pad.t - pad.b;

    // C(Θ) curve
    ctx.strokeStyle = "rgba(120,160,200,0.15)";
    ctx.lineWidth = 0.5;
    ctx.beginPath(); ctx.moveTo(pad.l, pad.t + h); ctx.lineTo(pad.l + w, pad.t + h); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(pad.l, pad.t); ctx.lineTo(pad.l + w, pad.t); ctx.stroke();

    ctx.strokeStyle = "#8bc4a0";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    for (let i = 0; i <= w; i++) {
      const theta = i / w;
      const val = C(theta);
      const y = pad.t + h - (val / 2) * h;
      i === 0 ? ctx.moveTo(pad.l + i, y) : ctx.lineTo(pad.l + i, y);
    }
    ctx.stroke();

    // Fibonacci wells
    const wells = [
      { theta: 13/120, label: "a₀", color: "#e07050" },
      { theta: 13/60, label: "α", color: "#c090e0" },
      { theta: 34/120, label: "H₀", color: "#60b0e0" },
      { theta: 60/120, label: "Λ", color: "#f0c040" },
    ];

    wells.forEach(({ theta, label, color }) => {
      const x = pad.l + theta * w;
      const val = C(theta);
      const y = pad.t + h - (val / 2) * h;
      ctx.strokeStyle = color + "60";
      ctx.lineWidth = 1;
      ctx.setLineDash([3, 3]);
      ctx.beginPath(); ctx.moveTo(x, pad.t + h); ctx.lineTo(x, y); ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = color;
      ctx.beginPath(); ctx.arc(x, y, 4, 0, 2 * Math.PI); ctx.fill();
      ctx.font = "bold 10px 'IBM Plex Mono', monospace";
      ctx.textAlign = "center";
      ctx.fillText(label, x, y - 10);
    });

    if (highlightTheta !== null && highlightTheta > 0 && highlightTheta < 1) {
      const x = pad.l + highlightTheta * w;
      const val = C(highlightTheta);
      const y = pad.t + h - (val / 2) * h;
      ctx.fillStyle = "#fff";
      ctx.beginPath(); ctx.arc(x, y, 5, 0, 2 * Math.PI); ctx.fill();
      ctx.strokeStyle = "#fff";
      ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(x, y, 5, 0, 2 * Math.PI); ctx.stroke();
    }

    // axis labels
    ctx.fillStyle = "rgba(180,200,220,0.7)";
    ctx.font = "10px 'IBM Plex Mono', monospace";
    ctx.textAlign = "center";
    ctx.fillText("0", pad.l, pad.t + h + 16);
    ctx.fillText("Θ", pad.l + w / 2, pad.t + h + 28);
    ctx.fillText("1", pad.l + w, pad.t + h + 16);
    ctx.textAlign = "right";
    ctx.fillText("2", pad.l - 6, pad.t + 6);
    ctx.fillText("0", pad.l - 6, pad.t + h + 4);
    ctx.fillText("C(Θ)", pad.l - 6, pad.t + h / 2);
  }, [width, height, highlightTheta]);

  return <canvas ref={canvasRef} style={{ width, height, display: "block" }} />;
}

function Tab({ label, active, onClick }) {
  return (
    <button
      onClick={onClick}
      style={{
        background: active ? "rgba(110,193,228,0.12)" : "transparent",
        color: active ? "#6ec1e4" : "rgba(180,200,220,0.6)",
        border: "none",
        borderBottom: active ? "2px solid #6ec1e4" : "2px solid transparent",
        padding: "10px 18px",
        cursor: "pointer",
        fontFamily: "'IBM Plex Mono', monospace",
        fontSize: "13px",
        fontWeight: active ? 600 : 400,
        letterSpacing: "0.5px",
        transition: "all 0.2s",
      }}
    >
      {label}
    </button>
  );
}

function Section({ title, children }) {
  return (
    <div style={{ marginBottom: 28 }}>
      <h3 style={{
        fontFamily: "'Cormorant Garamond', Georgia, serif",
        fontSize: 20,
        fontWeight: 500,
        color: "#c8dce8",
        marginBottom: 12,
        letterSpacing: "0.5px",
      }}>{title}</h3>
      {children}
    </div>
  );
}

function Table({ headers, rows, highlight }) {
  return (
    <div style={{ overflowX: "auto" }}>
      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13, fontFamily: "'IBM Plex Mono', monospace" }}>
        <thead>
          <tr>
            {headers.map((h, i) => (
              <th key={i} style={{
                textAlign: "left", padding: "8px 10px", color: "rgba(180,200,220,0.6)",
                borderBottom: "1px solid rgba(120,160,200,0.2)", fontWeight: 500, fontSize: 11,
                letterSpacing: "0.8px", textTransform: "uppercase"
              }}>{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, ri) => (
            <tr key={ri} style={{
              background: highlight === ri ? "rgba(110,193,228,0.08)" : ri % 2 === 0 ? "rgba(255,255,255,0.02)" : "transparent"
            }}>
              {row.map((cell, ci) => (
                <td key={ci} style={{
                  padding: "7px 10px", color: "#c8dce8",
                  borderBottom: "1px solid rgba(120,160,200,0.08)"
                }}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function NumberInput({ label, value, onChange, step = 1, min, max }) {
  return (
    <label style={{ display: "block", marginBottom: 14 }}>
      <span style={{
        display: "block", fontSize: 11, color: "rgba(180,200,220,0.6)",
        fontFamily: "'IBM Plex Mono', monospace", marginBottom: 4,
        letterSpacing: "0.5px", textTransform: "uppercase"
      }}>{label}</span>
      <input
        type="number"
        value={value}
        onChange={e => onChange(parseFloat(e.target.value) || 0)}
        step={step}
        min={min}
        max={max}
        style={{
          width: "100%", padding: "8px 10px", background: "rgba(255,255,255,0.05)",
          border: "1px solid rgba(120,160,200,0.2)", borderRadius: 4,
          color: "#c8dce8", fontFamily: "'IBM Plex Mono', monospace", fontSize: 14,
          outline: "none", boxSizing: "border-box",
        }}
      />
    </label>
  );
}

function SelectInput({ label, value, onChange, options }) {
  return (
    <label style={{ display: "block", marginBottom: 14 }}>
      <span style={{
        display: "block", fontSize: 11, color: "rgba(180,200,220,0.6)",
        fontFamily: "'IBM Plex Mono', monospace", marginBottom: 4,
        letterSpacing: "0.5px", textTransform: "uppercase"
      }}>{label}</span>
      <select
        value={value}
        onChange={e => onChange(e.target.value)}
        style={{
          width: "100%", padding: "8px 10px", background: "rgba(255,255,255,0.05)",
          border: "1px solid rgba(120,160,200,0.2)", borderRadius: 4,
          color: "#c8dce8", fontFamily: "'IBM Plex Mono', monospace", fontSize: 14,
          outline: "none", boxSizing: "border-box",
        }}
      >
        {options.map(o => <option key={o.value} value={o.value}>{o.label}</option>)}
      </select>
    </label>
  );
}

function CalculatorPanel() {
  const [preset, setPreset] = useState("custom");
  const [thetaNum, setThetaNum] = useState(13);
  const [thetaDen, setThetaDen] = useState(120);
  const [n, setN] = useState(1);
  const [nNum, setNNum] = useState(1);
  const [nDen, setNDen] = useState(1);
  const [omegaSource, setOmegaSource] = useState("H");

  useEffect(() => {
    if (preset === "alpha") { setThetaNum(13); setThetaDen(60); setNNum(1); setNDen(30); setOmegaSource("L"); }
    else if (preset === "a0") { setThetaNum(13); setThetaDen(120); setNNum(1); setNDen(1); setOmegaSource("H"); }
    else if (preset === "H0") { setThetaNum(34); setThetaDen(120); setNNum(1); setNDen(1); setOmegaSource("H"); }
    else if (preset === "lambda") { setThetaNum(60); setThetaDen(120); setNNum(2); setNDen(1); setOmegaSource("L"); }
  }, [preset]);

  const theta = thetaDen !== 0 ? thetaNum / thetaDen : 0;
  const nEff = nDen !== 0 ? nNum / nDen : 0;
  const sqrtOmega = omegaSource === "H" ? SQRT_OMEGA_H : SQRT_OMEGA_LAMBDA;
  const cVal = C(theta);
  const dilution = Math.pow(sqrtOmega, -nEff);
  const result = cVal * dilution;

  return (
    <div>
      <Section title="Scaling Law Calculator">
        <div style={{
          background: "rgba(110,193,228,0.06)", borderRadius: 8, padding: "16px 20px",
          border: "1px solid rgba(110,193,228,0.15)", marginBottom: 20, textAlign: "center",
          fontFamily: "'Cormorant Garamond', Georgia, serif", fontSize: 22, color: "#e0eaf0",
          letterSpacing: "1px"
        }}>
          A / A<sub>P</sub> ≈ C(Θ) · (√Ω)<sup>−n</sup>
        </div>

        <SelectInput label="Preset" value={preset} onChange={setPreset} options={[
          { value: "custom", label: "Custom" },
          { value: "alpha", label: "α  (fine structure)" },
          { value: "a0", label: "a₀  (acceleration scale)" },
          { value: "H0", label: "H₀  (Hubble parameter)" },
          { value: "lambda", label: "Λ  (cosmological constant)" },
        ]} />

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
          <NumberInput label="Θ numerator" value={thetaNum} onChange={v => { setThetaNum(v); setPreset("custom"); }} step={1} />
          <NumberInput label="Θ denominator" value={thetaDen} onChange={v => { setThetaDen(v); setPreset("custom"); }} step={1} min={1} />
          <NumberInput label="n numerator" value={nNum} onChange={v => { setNNum(v); setPreset("custom"); }} step={1} />
          <NumberInput label="n denominator" value={nDen} onChange={v => { setNDen(v); setPreset("custom"); }} step={1} min={1} />
        </div>

        <SelectInput label="Scale" value={omegaSource} onChange={v => { setOmegaSource(v); setPreset("custom"); }} options={[
          { value: "H", label: "Ω_H (Hubble, epoch-dependent)" },
          { value: "L", label: "Ω_Λ (de Sitter, epoch-independent)" },
        ]} />

        <div style={{
          background: "rgba(255,255,255,0.03)", borderRadius: 8, padding: 16,
          border: "1px solid rgba(120,160,200,0.15)", marginTop: 16
        }}>
          <Table headers={["Component", "Value"]} rows={[
            ["Θ", `${thetaNum}/${thetaDen} = ${theta.toFixed(6)}`],
            ["C(Θ) = 2 sin²(πΘ)", cVal.toFixed(6)],
            ["n", `${nNum}/${nDen} = ${nEff.toFixed(6)}`],
            ["√Ω", formatSci(sqrtOmega)],
            ["(√Ω)⁻ⁿ", formatSci(dilution)],
            ["A / Aₚ", formatSci(result)],
          ]} />
        </div>
      </Section>

      <Section title="Phase Operator C(Θ)">
        <DomainCanvas width={560} height={170} highlightTheta={theta} />
      </Section>
    </div>
  );
}

function TheoryPanel() {
  return (
    <div>
      <Section title="The Postulate">
        <div style={{
          background: "rgba(110,193,228,0.06)", borderRadius: 8, padding: "16px 20px",
          border: "1px solid rgba(110,193,228,0.15)", marginBottom: 16, textAlign: "center",
          fontFamily: "'Cormorant Garamond', Georgia, serif", fontSize: 20, color: "#e0eaf0",
        }}>
          S¹ = ∂(Möbius) ↪ S³, &nbsp; ∂S³ = ∅
        </div>
        <p style={pStyle}>
          The temporal edge bounds the Möbius surface embedded in hypersphere space. The space has no boundary. Everything derived traces to this topology.
        </p>
      </Section>

      <Section title="Five Foundations">
        <Table headers={["Foundation", "Statement"]} rows={[
          ["Wave-matter identity", "λ = h/p is identity. Matter is wave, sampled."],
          ["Surface origin", "Time is phase on the boundary of a 2D manifold."],
          ["Topology", "ψ(y + L) = −ψ(y). A field traversing the manifold returns to minus itself."],
          ["Bounded evaluation", "R_H / ℓ_P has definition at the limit ∞/0. The observer is the structural midpoint."],
          ["Embedded sampling", "The observable's character selects the manifold (n = 1, 2, 3). Dimension follows the measurement."],
        ]} />
      </Section>

      <Section title="The Cosmic Standing Wave">
        <div style={{
          textAlign: "center", fontFamily: "'Cormorant Garamond', Georgia, serif",
          fontSize: 22, color: "#e0eaf0", margin: "12px 0"
        }}>
          Ψ = cos(t/2)
        </div>
        <WaveCanvas width={560} height={180} />
        <p style={{ ...pStyle, marginTop: 12 }}>
          Anti-periodicity requires period 4π. Cosine is inherited because the universe initiates at maximum amplitude Ψ = +1. The present epoch sits at t ≈ 5.22 rad, approximately 2.8 Gyr before turnaround.
        </p>
      </Section>

      <Section title="The 120 Domain">
        <p style={pStyle}>
          The binary icosahedral group 2I is the largest exceptional discrete subgroup of SU(2) ≅ S³, with |2I| = 120. Five independent paths converge on 120 as the maximum resolution the space provides: group theory, number theory, musical consonance, angular partitioning, and irreducibility of F₇ = 13.
        </p>
        <Table headers={["Term", "Resolution", "Source"]} rows={[
          ["120 domain", "120 positions", "|2I| = 120 native to S³"],
          ["Grid", "120 (fermionic)", "Half-integer modes on the domain"],
          ["60R-grid", "60 positions (even only)", "|ψ|² projects 2I → I"],
        ]} />
      </Section>

      <Section title="Manifold Assignment">
        <Table headers={["n", "Manifold", "Observables", "(√Ω)⁻ⁿ"]} rows={[
          ["1", "Temporal edge S¹", "H₀, a₀", "~10⁻⁶¹"],
          ["2", "Möbius surface", "Λ", "~10⁻¹²²"],
          ["3/2", "Gauss-Codazzi interface", "Gravity", "—"],
          ["3", "Space S³", "Null 'dark matter'", "~10⁻¹⁸³"],
        ]} />
      </Section>
    </div>
  );
}

function ScorecardPanel() {
  return (
    <div>
      <Section title="Numerical Scorecard">
        <p style={pStyle}>
          Blind outputs of the scaling law, checked against observation. Zero free parameters.
        </p>
        <Table headers={["Observable", "Predicted", "Observed", "Agreement"]} rows={
          SCORECARD.map(s => [s.obs, s.predicted, s.observed, s.agr])
        } />
      </Section>

      <Section title="Fibonacci Wells">
        <Table headers={["Well", "Θ", "C(Θ)", "Grid", "n", "Observable"]} rows={
          WELLS.map(w => [w.pos, w.theta.toFixed(4), C(w.theta).toFixed(4), w.grid,
            w.n === 1/30 ? "1/30" : String(w.n), w.label + " — " + w.obs])
        } />
      </Section>

      <Section title="Falsification">
        <p style={pStyle}>
          MIT has no adjustable parameters. Discrepancies cannot be absorbed. The framework stands or falls on population-level agreement with locked predictions.
        </p>
        <Table headers={["Prediction", "Falsified if", "Threshold"]} rows={[
          ["a₀(z) ∝ H(z)", "a₀ consistent with constant at high z", "≥ 2σ, z > 2"],
          ["Λ constant", "ρ_DE(z) shows significant evolution", "≥ 2σ"],
          ["CMB suppression", "Wrong suppression scale", "ℓ_cut ∉ [15, 50]"],
        ]} />
        <div style={{
          marginTop: 16, padding: "12px 16px", borderRadius: 6,
          background: "rgba(240,192,64,0.08)", border: "1px solid rgba(240,192,64,0.2)",
          fontSize: 13, color: "#f0c040", fontFamily: "'IBM Plex Mono', monospace"
        }}>
          Falsification window: Euclid Data Release 1 — October 21, 2026
        </div>
      </Section>
    </div>
  );
}

function ResourcesPanel() {
  return (
    <div>
      <Section title="Publication Registry">
        <p style={pStyle}>All documents maintain DOI priority via Zenodo. Pre-registered predictions available for independent verification.</p>
        <Table headers={["Paper", "Category", "DOI"]} rows={[
          ["Mode Identity Theory v6", "Core", "10.5281/zenodo.18064856"],
          ["Team Cosine: Euclid DR1 2026", "Falsification", "10.5281/zenodo.18189078"],
          ["Yang–Mills Mass Gap on S³/2I", "Math structure", "10.5281/zenodo.18463584"],
          ["Riemann Hypothesis: Zeta Zeros", "Math structure", "10.5281/zenodo.18672160"],
          ["The Waltz: Λ Supplement", "Particle", "10.5281/zenodo.18176445"],
          ["α fine structure: Minimum Step", "Particle", "10.5281/zenodo.18484780"],
          ["The Spectrum: Particle Mass", "Particle", "10.5281/zenodo.18603975"],
          ["a₀ Evolving: High-z Masses", "Cosmology", "10.5281/zenodo.18072995"],
          ["w Evolving: Topological Resolution", "Cosmology", "10.5281/zenodo.18081581"],
          ["Axis Aligned: CMB Anomalies", "Cosmology", "10.5281/zenodo.18092169"],
          ["Λ Ground Mode", "Cosmology", "10.5281/zenodo.18307314"],
          ["H₀ Local: Hubble Tension", "Cosmology", "10.5281/zenodo.18363693"],
        ]} />
        <p style={{ ...pStyle, marginTop: 12, color: "rgba(180,200,220,0.5)", fontStyle: "italic" }}>
          1, 1, 2, 3, 5. The framework built on Fibonacci wells has a Fibonacci publication structure.
        </p>
      </Section>

      <Section title="Source Code">
        <p style={pStyle}>
          This calculator implements the complete MIT scaling law with zero hidden parameters. Every numerical output can be traced from the single topological postulate through the derivation chain. The code is the math.
        </p>
        <div style={{
          background: "rgba(255,255,255,0.03)", borderRadius: 6, padding: 16,
          fontFamily: "'IBM Plex Mono', monospace", fontSize: 12, color: "#8bc4a0",
          lineHeight: 1.7, border: "1px solid rgba(120,160,200,0.1)", overflowX: "auto"
        }}>
          <div style={{ color: "rgba(180,200,220,0.4)" }}>// The entire framework in four lines:</div>
          <div>C(Θ) = 2 sin²(πΘ)</div>
          <div>A/Aₚ = C(Θ) · (√Ω)⁻ⁿ</div>
          <div>Θ ∈ &#123;13, 21, 34, 55, 60&#125; / 120</div>
          <div>n ∈ &#123;1/30, 1, 3/2, 2, 3&#125;</div>
        </div>
      </Section>

      <Section title="Contact">
        <p style={pStyle}>
          blake shatto, p.e. — bshatto.pe@gmail.com
          <br />
          <span style={{ color: "rgba(180,200,220,0.5)" }}>modeidentitytheory.com</span>
        </p>
      </Section>
    </div>
  );
}

const pStyle = {
  fontFamily: "'IBM Plex Mono', monospace",
  fontSize: 13,
  color: "rgba(200,220,232,0.8)",
  lineHeight: 1.7,
  margin: "0 0 12px 0",
};

export default function App() {
  const [tab, setTab] = useState("calc");

  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(170deg, #0a0e14 0%, #0d1520 40%, #0a1018 100%)",
      color: "#c8dce8",
      fontFamily: "'IBM Plex Mono', monospace",
    }}>
      <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=IBM+Plex+Mono:wght@300;400;500;600&display=swap" rel="stylesheet" />

      {/* Header */}
      <div style={{
        padding: "32px 24px 20px",
        textAlign: "center",
        borderBottom: "1px solid rgba(120,160,200,0.1)"
      }}>
        <h1 style={{
          fontFamily: "'Cormorant Garamond', Georgia, serif",
          fontSize: 32,
          fontWeight: 300,
          letterSpacing: "3px",
          color: "#e0eaf0",
          margin: 0,
        }}>
          MODE IDENTITY THEORY
        </h1>
        <p style={{
          fontFamily: "'IBM Plex Mono', monospace",
          fontSize: 12,
          color: "rgba(180,200,220,0.5)",
          letterSpacing: "2px",
          marginTop: 8,
        }}>
          S¹ = ∂(Möbius) ↪ S³ &nbsp;·&nbsp; ∂S³ = ∅ &nbsp;·&nbsp; ONE POSTULATE &nbsp;·&nbsp; ZERO FREE PARAMETERS
        </p>
      </div>

      {/* Tabs */}
      <div style={{
        display: "flex",
        justifyContent: "center",
        borderBottom: "1px solid rgba(120,160,200,0.1)",
        flexWrap: "wrap",
      }}>
        <Tab label="CALCULATOR" active={tab === "calc"} onClick={() => setTab("calc")} />
        <Tab label="THEORY" active={tab === "theory"} onClick={() => setTab("theory")} />
        <Tab label="SCORECARD" active={tab === "score"} onClick={() => setTab("score")} />
        <Tab label="REGISTRY" active={tab === "registry"} onClick={() => setTab("registry")} />
      </div>

      {/* Content */}
      <div style={{ maxWidth: 640, margin: "0 auto", padding: "24px 20px 48px" }}>
        {tab === "calc" && <CalculatorPanel />}
        {tab === "theory" && <TheoryPanel />}
        {tab === "score" && <ScorecardPanel />}
        {tab === "registry" && <ResourcesPanel />}
      </div>

      {/* Footer */}
      <div style={{
        textAlign: "center",
        padding: "20px 24px 32px",
        borderTop: "1px solid rgba(120,160,200,0.08)",
        fontFamily: "'Cormorant Garamond', Georgia, serif",
        fontSize: 14,
        fontStyle: "italic",
        color: "rgba(180,200,220,0.4)",
        letterSpacing: "0.5px",
      }}>
        The identity is the wave Ψ
      </div>
    </div>
  );
}
