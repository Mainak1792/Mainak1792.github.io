"""Page bodies for the Happy Steps site."""

def ic(name, extra=""):
    P = {
        "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/>',
        "eyeoff": '<path d="M3 3l18 18"/><path d="M10.6 6.1A10 10 0 0 1 12 6c5 0 9 6 9 6a17 17 0 0 1-3.2 3.8"/><path d="M6.5 7.6C4.3 9.2 3 12 3 12s4 6 9 6a9 9 0 0 0 4.4-1.1"/>',
        "steps": '<ellipse cx="8.5" cy="9" rx="2.6" ry="4.2" transform="rotate(-12 8.5 9)"/><ellipse cx="15.5" cy="14" rx="2.6" ry="4.2" transform="rotate(12 15.5 14)"/>',
        "spark": '<path d="M12 3l1.9 5.6L19.5 10.5l-5.6 1.9L12 18l-1.9-5.6L4.5 10.5l5.6-1.9z"/><path d="M19 17l.7 1.8 1.8.7-1.8.7-.7 1.8-.7-1.8-1.8-.7 1.8-.7z"/>',
        "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
        "trend": '<path d="M4 18l5-6 4 3 7-8"/><path d="M15 7h5v5"/>',
        "bell": '<path d="M6 16v-5a6 6 0 1 1 12 0v5l2 2H4l2-2z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
        "speaker": '<path d="M4 9h4l5-4v14l-5-4H4z"/><path d="M16 9a4 4 0 0 1 0 6"/><path d="M18.5 6.5a7.5 7.5 0 0 1 0 11"/>',
        "home": '<path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-6h4v6"/>',
        "hospital": '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M12 8v8M8 12h8"/>',
        "chip": '<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M9 3v4M15 3v4M9 17v4M15 17v4M3 9h4M3 15h4M17 9h4M17 15h4"/>',
        "wave": '<path d="M3 12h3l2-6 3 12 3-9 2 3h5"/>',
        "plug": '<path d="M9 15l6-6"/><path d="M7 11l-2 2a3 3 0 0 0 4 4l2-2"/><path d="M17 13l2-2a3 3 0 0 0-4-4l-2 2"/>',
        "quake": '<path d="M3 20h18"/><path d="M6 20V10l6-5 6 5v10"/><path d="M11 11l2 2-2 2 2 2"/>',
        "moon": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
        "arrow": '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
        "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
        "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
        "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
        "check": '<path d="M5 12l5 5 9-10"/>',
        "flask": '<path d="M9 3h6M10 3v6L4.5 18.5A2 2 0 0 0 6.2 21.5h11.6a2 2 0 0 0 1.7-3L14 9V3"/><path d="M7 15h10"/>',
        "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/>',
        "people": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6.5 6.5 0 0 1 3.5 6"/>',
        "play": '<path d="M8 5v14l11-7z" fill="currentColor"/>',
        "scale": '<path d="M4 20h16"/><rect x="5" y="12" width="3" height="6"/><rect x="10.5" y="8" width="3" height="10"/><rect x="16" y="4" width="3" height="14"/>',
    }
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" {extra}>{P[name]}</svg>')

APPICON = """<svg class="app" viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="ai" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1A73E8"/><stop offset="1" stop-color="#1E8E3E"/></linearGradient></defs><rect width="32" height="32" rx="9" fill="url(#ai)"/><ellipse cx="11.6" cy="12.4" rx="3.1" ry="4.9" fill="#fff" transform="rotate(-14 11.6 12.4)"/><ellipse cx="20.4" cy="15.6" rx="3.1" ry="4.9" fill="#fff" fill-opacity=".82" transform="rotate(14 20.4 15.6)"/><path d="M10.2 24.2q5.8 3.4 11.6 0" stroke="#fff" stroke-width="2.2" fill="none" stroke-linecap="round"/></svg>"""

CTA = """
<section class="section tight"><div class="wrap">
  <div class="cta-band reveal">
    <div><h2>See a real footstep become a kind word.</h2>
      <p>The live demo runs real floor recordings through the full pipeline and calls Gemini in your browser.</p></div>
    <div class="btns"><a class="btn btn-primary btn-lg" href="demo.html">Open the live demo</a>
      <a class="btn btn-outline btn-lg" href="how-it-works.html">How it works</a></div>
  </div>
</div></section>"""

# ======================================================================
INDEX = """
<section class="hero">
  <div class="wrap split">
    <div>
      <span class="eyebrow">""" + ic("spark", 'width="16" height="16"') + """ Ambient care, powered by Gemini</span>
      <h1 class="display">Every step says <em>“I’m okay.”</em></h1>
      <p class="lead">Happy Steps turns the footsteps your parents already take into a kind daily note for the family. No cameras. No microphones. Nothing to wear.</p>
      <p class="ja">毎日の足音を、家族へのやさしいメッセージに。カメラも、マイクも、身につける機器もいりません。</p>
      <div class="btns">
        <a class="btn btn-primary btn-lg" href="demo.html">""" + ic("play") + """ Try the live demo</a>
        <a class="btn btn-outline btn-lg" href="how-it-works.html">See how it works</a>
      </div>
      <div class="meta">
        <span>""" + ic("eyeoff") + """ No images, no audio</span>
        <span>""" + ic("chip") + """ Signal stays in the home</span>
        <span>""" + ic("heart") + """ Never diagnoses</span>
      </div>
    </div>
    <div class="hv" aria-label="Product preview: a floor signal becomes a short summary, then a message to the family">
      <div class="hv-card">
        <div class="hv-head"><span class="live-dot"></span> Living room floor · geophone <span class="right">real recording · 7 s</span></div>
        <canvas id="heroWave" aria-hidden="true"></canvas>
        <div class="hv-foot"><span><b class="num" id="heroSteps">0</b> steps</span><span><b>111</b> steps/min</span><span><b>Resident</b> recognised</span></div>
      </div>
      <div class="hv-json"><code>{<span class="k">"person"</span>:<span class="s">"resident_01"</span>, <span class="k">"steps"</span>:<span class="n">17</span>, <span class="k">"cadence_spm"</span>:<span class="n">111</span>, …}</code><small>~300 bytes leave home</small></div>
      <div class="hv-card hv-note">""" + APPICON + """
        <div><div class="top"><b>Happy Steps</b> · now</div>
          <h4>お母さんは今日も元気に歩いています</h4>
          <p>Mother is walking well today. Her pace is steady, and she rested well last night.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="tight" style="padding:28px 0;border-top:1px solid var(--line-2);border-bottom:1px solid var(--line-2)">
  <div class="wrap trust">
    <span>Built on <b>5+ years</b> of PhD research</span><span class="sep"></span>
    <span><b>100-person</b> footstep dataset</span><span class="sep"></span>
    <span>Runs on a <b>Raspberry Pi</b></span><span class="sep"></span>
    <span><b>Gemini API</b> with function calling &amp; voice</span>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">THE PROBLEM</span>
      <h2 class="h2">More parents live alone. Families worry from far away.</h2>
      <p class="lead">Japan is the first country to face this at scale. Most of us cannot call every day, and most parents do not want to be watched.</p>
    </div>
    <div class="grid g3" style="margin-top:56px">
      <div class="stat blue reveal"><b class="num">7.4M</b><p class="what">people aged 65+ lived alone in Japan in 2020.</p><p class="src">National Institute of Population and Social Security Research</p></div>
      <div class="stat green reveal"><b class="num">10.8M</b><p class="what">expected to live alone by 2050, one in five households.</p><p class="src">IPSS household projection, 2024</p></div>
      <div class="stat red reveal"><b class="num">58,044</b><p class="what">older people died alone at home in 2024, many found days later.</p><p class="src">National Police Agency, 2025</p></div>
    </div>

    <div class="section-head reveal" style="margin-top:96px">
      <h2 class="h2">Today’s options ask too much.</h2>
      <p class="lead">Cameras feel like being watched. Wearables get forgotten or run flat. A help button only works if you can press it.</p>
    </div>
    <div class="table-wrap reveal" style="margin-top:32px">
      <table class="t">
        <thead><tr><th></th><th class="us">Happy Steps</th><th>Home camera</th><th>Smartwatch</th><th>Help button</th></tr></thead>
        <tbody>
          <tr><td>Nothing to wear or charge</td><td class="us">Yes</td><td class="yes">Yes</td><td class="no">No</td><td class="no">No</td></tr>
          <tr><td>No images or sound recorded</td><td class="us">Yes</td><td class="no">No</td><td class="yes">Yes</td><td class="yes">Yes</td></tr>
          <tr><td>Works if the person cannot ask for help</td><td class="us">Yes · impact, then silence</td><td class="yes">Yes</td><td class="meh">Only if worn</td><td class="no">No</td></tr>
          <tr><td>Notices slow change over weeks</td><td class="us">Yes · personal baseline</td><td class="meh">Hard to review</td><td class="meh">Only if worn</td><td class="no">No</td></tr>
          <tr><td>Knows who is walking</td><td class="us">Yes · footstep signature</td><td class="yes">Yes</td><td class="yes">Yes</td><td class="no">No</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section gray">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="kicker">THE PRODUCT</span>
      <h2 class="h2">One small sensor. Three kind outcomes.</h2>
      <p class="ja">小さなセンサー１つで、３つのやさしさ。</p>
    </div>
    <div class="grid g3" style="margin-top:56px">
      <div class="card reveal"><div class="icon-chip green">""" + ic("heart") + """</div><h3>A daily note for the family</h3>
        <p>Each evening the family gets a short, warm update in plain words: how she walked, how she slept, anything new.</p></div>
      <div class="card reveal"><div class="icon-chip red">""" + ic("bell") + """</div><h3>A gentle alert when it matters</h3>
        <p>A heavy impact followed by silence, or an unusually quiet day, becomes a clear request to check in, with a suggested action.</p></div>
      <div class="card reveal"><div class="icon-chip">""" + ic("speaker") + """</div><h3>A friendly voice for her</h3>
        <p>Gemini speaks a short, cheerful message at home: “You walked well today.” Care that talks to her, not only about her.</p></div>
    </div>

    <div class="feature reveal" style="margin-top:24px">
      <div class="txt">
        <span class="kicker">PERSONAL, NOT AVERAGE</span>
        <h3 class="h2" style="margin-top:12px">“Slower” means slower than <i>her</i> usual days.</h3>
        <p class="lead" style="margin-top:16px">Gemini compares today with the resident’s own last two weeks. Small changes in pace, rhythm or night-time walking become early, gentle signals, long before they become emergencies.</p>
        <ul class="checks">
          <li><span><b>Walking speed</b> and steadiness of rhythm</span></li>
          <li><span><b>Night walks</b> between midnight and 5 a.m.</span></li>
          <li><span><b>Quiet hours</b> with no movement at all</span></li>
          <li><span><b>Visitors</b>, recognised as “not the resident”</span></li>
        </ul>
      </div>
      <div class="vis">
        <div class="phone" aria-label="Example messages on a family member's phone">
          <div class="sb"><span>18:30</span><span>Happy Steps</span></div>
          <div class="msg good"><div class="who">""" + ic("check", 'width="14" height="14"') + """ Mon</div><h5>今日も元気に歩いています</h5><p>Usual pace, slept through the night.</p></div>
          <div class="msg watch"><div class="who">""" + ic("moon", 'width="14" height="14"') + """ Tue</div><h5>夜中に何度か起きていたようです</h5><p>Up 3 times at night. Usually 0.</p></div>
          <div class="msg watch"><div class="who">""" + ic("trend", 'width="14" height="14"') + """ Wed</div><h5>いつもより、ゆっくり歩いていました</h5><p>Pace 95 vs usual 111 steps/min.</p></div>
          <div class="msg alert"><div class="who">""" + ic("bell", 'width="14" height="14"') + """ Now</div><h5>様子を確かめてください</h5><p>Heavy impact at 10:04, no steps since.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">HOW IT WORKS</span>
      <h2 class="h2">From a footstep to a kind word.</h2>
      <p class="lead">The hard signal work happens inside the home. Gemini does the human part.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><div class="n">01 · SENSE</div><h3>Feel the floor</h3><p>A geophone on the floor feels each step as a tiny vibration.</p><span class="ja">床の振動を感じる</span></div>
      <div class="step reveal"><div class="n">02 · UNDERSTAND</div><h3>Read each step at home</h3><p>A small edge device finds steps, who is walking, and how.</p><span class="ja">家の中で一歩ずつ読み取る</span></div>
      <div class="step reveal"><div class="n">03 · SUMMARISE</div><h3>Send only numbers</h3><p>About 300 bytes per walk leave the home. Never the raw signal.</p><span class="ja">数字だけを送る</span></div>
      <div class="step reveal"><div class="n">04 · CARE</div><h3>Gemini writes and speaks</h3><p>Gemini compares with her usual days, chooses an action, and writes kindly.</p><span class="ja">Geminiがやさしく伝える</span></div>
    </div>
    <p style="margin-top:32px"><a class="btn btn-tonal" href="how-it-works.html">Explore the architecture """ + ic("arrow") + """</a></p>
  </div>
</section>

<section class="section gray">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">WHY GEMINI</span>
      <h2 class="h2" style="margin-top:12px">The right job for each part.</h2>
      <p class="lead" style="margin-top:16px">Gemini is not asked to read raw vibration. A small, proven model at home does that. Gemini does what it is best at: judging change over time, choosing an action, and speaking to people with warmth.</p>
      <ul class="checks">
        <li><span><b>Long-context reasoning</b> over today plus a 14-day personal baseline</span></li>
        <li><span><b>Function calling</b> that plugs into any app: LINE, email, a care-home dashboard</span></li>
        <li><span><b>Natural Japanese and English</b> for families across borders</span></li>
        <li><span><b>Text-to-speech</b> for a friendly voice in the home</span></li>
      </ul>
    </div>
    <div class="code-card reveal">
      <div class="bar"><i></i><i></i><i></i> gemini · function call</div>
<pre class="code"><span class="c">// Gemini must pick exactly one action</span>
{
  <span class="k">"name"</span>: <span class="s">"send_family_report"</span>,
  <span class="k">"args"</span>: {
    <span class="k">"status"</span>: <span class="s">"gentle_watch"</span>,
    <span class="k">"headline_ja"</span>: <span class="s">"夜中に何度か起きていたようです"</span>,
    <span class="k">"headline_en"</span>: <span class="s">"She was up a few times at night"</span>,
    <span class="k">"changes"</span>: [{
      <span class="k">"metric"</span>: <span class="s">"walks at night"</span>,
      <span class="k">"today"</span>: <span class="s">"4"</span>, <span class="k">"usual"</span>: <span class="s">"0.2"</span> }],
    <span class="k">"message_to_resident_ja"</span>:
      <span class="s">"今夜はゆっくり眠れるといいですね。"</span>
  }
}</pre>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="kicker">RESEARCH FOUNDATION</span>
      <h2 class="h2">Not an idea on paper. Years of measured results.</h2>
      <p class="lead">Happy Steps is built on doctoral research in floor-vibration sensing, published in IEEE and Nature-portfolio journals. Lab results:</p>
    </div>
    <div class="grid g4" style="margin-top:48px">
      <div class="metric reveal"><b class="num">92.7%</b><span>correct person, out of 100+</span><small>Rank-1 identification, DeepStep</small></div>
      <div class="metric reveal"><b class="num">93.8%</b><span>AUC for spotting strangers</span><small>Open-set detection</small></div>
      <div class="metric reveal"><b class="num">93.7%</b><span>gait-abnormality detection</span><small>Multi-task model</small></div>
      <div class="metric reveal"><b class="num">0.78 s</b><span>per step on a Raspberry Pi</span><small>22 MB model, fully on device</small></div>
    </div>
    <p style="margin-top:32px"><a class="btn btn-tonal" href="technology.html">Read the technology """ + ic("arrow") + """</a></p>
  </div>
</section>

<section class="section gray">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="kicker">WHERE IT GOES NEXT</span>
      <h2 class="h2">Every building already has a floor.</h2>
    </div>
    <div class="grid g4" style="margin-top:56px">
      <div class="card reveal"><div class="icon-chip green">""" + ic("home") + """</div><h3>Homes</h3><p>Parents living alone, and families living far away.</p></div>
      <div class="card reveal"><div class="icon-chip">""" + ic("people") + """</div><h3>Care homes</h3><p>Quiet night rounds without cameras in private rooms.</p></div>
      <div class="card reveal"><div class="icon-chip yellow">""" + ic("hospital") + """</div><h3>Hospitals</h3><p>Early signs of change in walking during recovery.</p></div>
      <div class="card reveal"><div class="icon-chip red">""" + ic("quake") + """</div><h3>Disasters</h3><p>After an earthquake, which rooms still have people moving.</p></div>
    </div>
  </div>
</section>
""" + CTA

# ======================================================================
ARCH_SVG = """<svg viewBox="0 0 1100 420" role="img" aria-labelledby="archT">
<title id="archT">Architecture: floor sensor and edge device inside the home; only JSON events cross to the Gemini API; Gemini calls one of two functions that reach the family app and the home speaker.</title>
<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#5F6368"/></marker></defs>
<style>.b{fill:#fff;stroke:#DADCE0;stroke-width:1.5}.t{font:500 15px 'Google Sans Flex','Roboto Flex',sans-serif;fill:#202124}.s{font:400 12.5px 'Roboto Flex',sans-serif;fill:#5F6368}.l{stroke:#5F6368;stroke-width:1.6;fill:none;marker-end:url(#ar)}.k{font:500 12px 'Roboto Flex',sans-serif;letter-spacing:.08em}</style>
<rect x="10" y="20" width="520" height="380" rx="28" fill="#E6F4EA"/>
<text x="34" y="52" class="k" fill="#188038">INSIDE THE HOME</text>
<rect x="580" y="20" width="510" height="380" rx="28" fill="#E8F0FE"/>
<text x="604" y="52" class="k" fill="#174EA6">CLOUD · GEMINI API</text>
<line x1="555" y1="30" x2="555" y2="390" stroke="#9AA0A6" stroke-dasharray="6 6" stroke-width="1.5"/>
<rect class="b" x="34" y="80" width="150" height="76" rx="16"/><text x="56" y="113" class="t">Geophone</text><text x="56" y="135" class="s">floor vibration</text>
<rect class="b" x="34" y="196" width="470" height="182" rx="18"/>
<text x="56" y="226" class="t">Edge device · Raspberry Pi</text>
<rect x="56" y="242" width="132" height="56" rx="12" fill="#F8F9FA"/><text x="70" y="266" class="t" style="font-size:13px">Step isolation</text><text x="70" y="284" class="s">GMM / EM</text>
<rect x="198" y="242" width="132" height="56" rx="12" fill="#F8F9FA"/><text x="212" y="266" class="t" style="font-size:13px">Time–frequency</text><text x="212" y="284" class="s">CWT · Morlet</text>
<rect x="340" y="242" width="144" height="56" rx="12" fill="#F8F9FA"/><text x="354" y="266" class="t" style="font-size:13px">Who &amp; how</text><text x="354" y="284" class="s">DeepStep · gait</text>
<rect x="56" y="312" width="428" height="48" rx="12" fill="#1F2023"/><text x="74" y="341" style="font:500 13px 'Roboto Mono',monospace;fill:#81C995">footstep-event/v1  ·  ~300 bytes per walk</text>
<path class="l" d="M109 156v38"/>
<path class="l" d="M188 270h8"/><path class="l" d="M330 270h8"/>
<rect class="b" x="264" y="80" width="240" height="76" rx="16"/><text x="286" y="113" class="t">Home speaker</text><text x="286" y="135" class="s">kind voice for the resident</text>
<path class="l" d="M484 336h120"/>
<text x="500" y="326" class="s">only JSON</text>
<rect class="b" x="606" y="290" width="230" height="86" rx="16"/><text x="628" y="322" class="t">Gemini reasoning</text><text x="628" y="344" class="s">today vs 14-day baseline</text><text x="628" y="362" class="s">forced function calling</text>
<rect class="b" x="606" y="80" width="230" height="76" rx="16"/><text x="628" y="113" class="t">Gemini text-to-speech</text><text x="628" y="135" class="s">Japanese voice</text>
<rect class="b" x="866" y="80" width="200" height="86" rx="16"/><text x="886" y="112" class="t">send_family_report</text><text x="886" y="134" class="s">daily note · gentle watch</text>
<rect class="b" x="866" y="196" width="200" height="86" rx="16"/><text x="886" y="228" class="t">raise_alert</text><text x="886" y="250" class="s">check in · urgent</text>
<rect class="b" x="866" y="304" width="200" height="72" rx="16"/><text x="886" y="336" class="t">Family app</text><text x="886" y="356" class="s">LINE · email · dashboard</text>
<path class="l" d="M836 318C850 250 850 150 864 125"/><path class="l" d="M836 330C852 290 852 250 864 240"/>
<path class="l" d="M966 282v20"/><path class="l" d="M966 166v28"/>
<path class="l" d="M721 290v-132"/>
<path class="l" d="M606 118H506"/>
</svg>"""

HOW = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">How it works</span>
  <h1 class="h1">From a footstep to a kind word, in five stages.</h1>
  <p class="lead">Happy Steps splits the work in two. Signal processing stays inside the home, on a small device. Only a short summary goes to Gemini, which reasons, decides and speaks.</p>
  <p class="ja">信号処理は家の中で。Geminiには短いまとめだけを送ります。</p>
</div></section>

<section class="section tight" style="padding-top:24px"><div class="wrap">
  <div class="figure reveal">""" + ARCH_SVG + """</div>
  <p class="figcap">The dashed line is the home boundary. Raw vibration never crosses it.</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="stage reveal">
    <div class="no">01</div>
    <div><h3>Sense the floor</h3><span class="ja">床の振動を感じる</span>
      <p>A geophone lies on the floor. When someone walks, each heel strike makes the floor move by about a millionth of a metre per second. The geophone turns that motion into a voltage, which we sample at 2–8 kHz.</p>
      <div class="where"><span class="pill green">In the home</span> <span class="pill gray">No camera · no microphone</span></div></div>
    <div class="card flat"><h3>Why the floor?</h3><p>A floor carries footsteps for several metres, so one sensor can cover a room. It sees nothing and hears no speech. It only feels force on the floor.</p></div>
  </div>

  <div class="stage reveal">
    <div class="no">02</div>
    <div><h3>Understand each step, at the edge</h3><span class="ja">家の中で一歩ずつ読み取る</span>
      <p>A Raspberry Pi isolates each footstep from background vibration, turns it into a time–frequency picture with a continuous wavelet transform, and runs DeepStep, a 22 MB model, to answer two questions: <b>who</b> is walking, and <b>how</b>.</p>
      <div class="where"><span class="pill green">In the home</span> <span class="pill gray">~0.8 s per step</span></div></div>
    <div class="card flat"><h3>What it measures</h3>
      <ul class="checks" style="margin-top:12px">
        <li><span><b>Identity</b>: the resident, or someone new (open-set)</span></li>
        <li><span><b>Pace</b>: steps per minute</span></li>
        <li><span><b>Steadiness</b>: how even the step timing is</span></li>
        <li><span><b>Balance of rhythm</b>: left–right timing symmetry</span></li>
      </ul></div>
  </div>

  <div class="stage reveal">
    <div class="no">03</div>
    <div><h3>Summarise to a tiny event</h3><span class="ja">数字だけのまとめにする</span>
      <p>When a walk ends, the device writes one small JSON event. Every home, floor and sensor uses the same format, so one home and one thousand homes look the same to the cloud.</p>
      <div class="where"><span class="pill blue">Crosses the boundary</span> <span class="pill gray">~8 KB a day instead of ~350 MB raw</span></div></div>
    <div class="code-card"><div class="bar"><i></i><i></i><i></i> footstep-event/v1</div>
<pre class="code">{
  <span class="k">"schema"</span>: <span class="s">"footstep-event/v1"</span>,
  <span class="k">"home_id"</span>: <span class="s">"H001"</span>,
  <span class="k">"time"</span>: <span class="s">"2026-11-01T10:00:42+09:00"</span>,
  <span class="k">"duration_s"</span>: <span class="n">8.3</span>,
  <span class="k">"person"</span>: <span class="s">"resident_01"</span>,
  <span class="k">"id_similarity"</span>: <span class="n">0.97</span>,
  <span class="k">"steps"</span>: <span class="n">17</span>,
  <span class="k">"cadence_spm"</span>: <span class="n">114</span>,
  <span class="k">"step_interval_cv"</span>: <span class="n">0.041</span>,
  <span class="k">"temporal_symmetry"</span>: <span class="n">0.97</span>,
  <span class="k">"event_type"</span>: <span class="s">"walk"</span>,
  <span class="k">"raw_signal_included"</span>: <span class="n">false</span>
}</pre></div>
  </div>

  <div class="stage reveal">
    <div class="no">04</div>
    <div><h3>Reason with Gemini</h3><span class="ja">Geminiが「いつも」と比べる</span>
      <p>Gemini receives today’s events and the resident’s 14-day baseline. A system instruction keeps it kind and careful: never diagnose, treat unknown people as visitors, suggest simple human actions. Function calling is set to <code>ANY</code>, so Gemini must choose one action.</p>
      <div class="where"><span class="pill blue">Gemini API</span> <span class="pill gray">function calling · JSON</span></div></div>
    <div class="code-card"><div class="bar"><i></i><i></i><i></i> request · generateContent</div>
<pre class="code">{
  <span class="k">"systemInstruction"</span>: { … },
  <span class="k">"contents"</span>: [{ <span class="k">"parts"</span>: [{ <span class="k">"text"</span>: <span class="s">"today + baseline JSON"</span> }] }],
  <span class="k">"tools"</span>: [{ <span class="k">"functionDeclarations"</span>: [
    { <span class="k">"name"</span>: <span class="s">"send_family_report"</span>, … },
    { <span class="k">"name"</span>: <span class="s">"raise_alert"</span>, … }
  ]}],
  <span class="k">"toolConfig"</span>: {
    <span class="k">"functionCallingConfig"</span>: { <span class="k">"mode"</span>: <span class="s">"ANY"</span> }
  }
}</pre></div>
  </div>

  <div class="stage reveal">
    <div class="no">05</div>
    <div><h3>Speak and deliver</h3><span class="ja">家族へ届け、本人に語りかける</span>
      <p>The function call goes to the family through any channel: a messaging app, email, or a care-home dashboard. The message for the resident is spoken at home with Gemini text-to-speech, in a warm Japanese voice.</p>
      <div class="where"><span class="pill blue">Gemini TTS</span> <span class="pill green">Home speaker</span></div></div>
    <div class="card flat"><h3>Two calls, any app</h3><p><code>send_family_report</code> for usual days and small changes. <code>raise_alert</code> when someone should check soon. Integrators only need to handle these two calls.</p></div>
  </div>
</div></section>

<section class="section gray"><div class="wrap">
  <div class="section-head reveal"><span class="kicker">BUILT TO SCALE</span><h2 class="h2">Designed to grow from one home to a city.</h2></div>
  <div class="grid g3" style="margin-top:48px">
    <div class="card reveal"><div class="icon-chip">""" + ic("plug") + """</div><h3>One open format</h3><p>Any sensor that can write <code>footstep-event/v1</code> can join: geophones, accelerometers, smart flooring.</p></div>
    <div class="card reveal"><div class="icon-chip green">""" + ic("chip") + """</div><h3>Cheap at the edge</h3><p>A sensor and a Raspberry Pi per room. No GPU, no streaming, very little bandwidth.</p></div>
    <div class="card reveal"><div class="icon-chip yellow">""" + ic("scale") + """</div><h3>Light in the cloud</h3><p>One Gemini call per home per day, plus rare alerts. Cost grows with homes, not with hours of signal.</p></div>
  </div>
</div></section>
""" + CTA

# ======================================================================
TECH = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow green">Technology</span>
  <h1 class="h1">Footsteps are a signal. We learned to read it.</h1>
  <p class="lead">Every step is a short burst of force that rings through the floor. Happy Steps separates the person from the floor, and turns what is left into identity, gait and change over time.</p>
  <p class="ja">足音は信号です。床の響きから「人」を取り出します。</p>
</div></section>

<section class="section tight"><div class="wrap split">
  <div class="reveal">
    <span class="kicker">THE PHYSICS</span>
    <h2 class="h2" style="margin-top:12px">Source × filter, like a voice.</h2>
    <p class="lead" style="margin-top:16px">In speech, sound is a source (the vocal cords) shaped by a filter (the vocal tract). A footstep works the same way. The foot strike is the source. The floor is the filter.</p>
    <p style="margin-top:16px;color:var(--ink-2)">The same person sounds different on wood and on concrete, just as one speaker sounds different through two microphones. The slow envelope of the floor response follows the force of the foot, so separating person from floor becomes a blind deconvolution problem. Solving it is what makes the method work in real homes.</p>
  </div>
  <div class="card reveal" style="padding:28px">
    <svg viewBox="0 0 480 220" role="img" aria-label="Diagram: foot strike force (source) passes through the floor response (filter) to give the measured vibration">
      <style>.tt{font:500 14px 'Google Sans Flex','Roboto Flex',sans-serif;fill:#202124}.ss{font:400 12px 'Roboto Flex',sans-serif;fill:#5F6368}</style>
      <rect x="10" y="40" width="120" height="110" rx="16" fill="#E8F0FE"/><path d="M28 120 L50 120 L58 70 L66 112 L76 96 L112 120" stroke="#1A73E8" stroke-width="2.5" fill="none"/>
      <text x="22" y="176" class="tt">Foot strike</text><text x="22" y="194" class="ss">source · the person</text>
      <text x="146" y="102" class="tt" style="font-size:24px">×</text>
      <rect x="180" y="40" width="120" height="110" rx="16" fill="#E6F4EA"/><path d="M196 95 q8-40 16 0 t16 0 t16 0 t16 0 t16 0 t8 0" stroke="#188038" stroke-width="2.5" fill="none"/>
      <text x="192" y="176" class="tt">Floor</text><text x="192" y="194" class="ss">filter · wood, concrete…</text>
      <text x="316" y="102" class="tt" style="font-size:24px">=</text>
      <rect x="350" y="40" width="120" height="110" rx="16" fill="#F8F9FA"/><path d="M362 95 l8 0 l4 -40 l4 75 l4 -60 l4 45 l4 -30 l4 20 l4 -12 l6 6 l8 -4 l8 2 l10 0 l10 0 l10 0" stroke="#202124" stroke-width="2" fill="none"/>
      <text x="362" y="176" class="tt">What we measure</text><text x="362" y="194" class="ss">geophone signal</text>
    </svg>
  </div>
</div></section>

<section class="section gray"><div class="wrap">
  <div class="section-head reveal"><span class="kicker">THE PIPELINE</span><h2 class="h2">Five steps from vibration to meaning.</h2></div>
  <div class="grid g3" style="margin-top:48px">
    <div class="card reveal"><div class="icon-chip">""" + ic("wave") + """</div><h3>1 · Footstep isolation</h3><p>An unsupervised Gaussian mixture, fitted with EM, separates footstep events from background vibration. No labels needed.</p></div>
    <div class="card reveal"><div class="icon-chip">""" + ic("scale") + """</div><h3>2 · Time–frequency view</h3><p>A continuous wavelet transform with a complex Morlet wavelet shows each step as a picture: sharp in time at high pitch, fine in frequency at low pitch.</p></div>
    <div class="card reveal"><div class="icon-chip green">""" + ic("user") + """</div><h3>3 · DeepStep identity</h3><p>A residual network with attention, trained with a contrastive open-set loss, says who walked, or that this is someone new.</p></div>
    <div class="card reveal"><div class="icon-chip yellow">""" + ic("trend") + """</div><h3>4 · Gait health</h3><p>A multi-task ResNet-18 flags unusual gait. Step timing gives pace, steadiness and rhythm balance.</p></div>
    <div class="card reveal"><div class="icon-chip red">""" + ic("flask") + """</div><h3>5 · Cognitive load (research)</h3><p>A dual-task walking study shows the mind’s load changes the footstep, something that usually needs EEG or questionnaires.</p></div>
    <div class="card reveal"><div class="icon-chip">""" + ic("spark") + """</div><h3>+ Gemini on top</h3><p>The outputs become small events. Gemini reasons over them across days, and talks to people.</p></div>
  </div>
</div></section>

<section class="section" id="results"><div class="wrap">
  <div class="section-head reveal"><span class="kicker">RESULTS</span><h2 class="h2">Measured, not promised.</h2>
    <p class="lead">From the VIBeID dataset: 100+ participants, 96+ hours of footsteps, recorded on wood, carpet, cement and outdoor surfaces at different walking speeds.</p></div>
  <div class="table-wrap reveal" style="margin-top:40px">
    <table class="t">
      <thead><tr><th>Task</th><th>Result</th><th>What it means</th></tr></thead>
      <tbody>
        <tr><td>Person identification (100+ people)</td><td class="num"><b>92.68%</b> Rank-1</td><td>About 1 wrong in 14</td></tr>
        <tr><td>Spotting an unknown person (open-set)</td><td class="num"><b>93.83%</b> AUC</td><td>Visitors are recognised as “not the resident”</td></tr>
        <tr><td>Gait-abnormality detection</td><td class="num"><b>93.67%</b></td><td>About 1 missed in 16</td></tr>
        <tr><td>Cognitive load from walking</td><td class="num"><b>68.49%</b></td><td>Better than 2-to-1 odds over chance; early research</td></tr>
        <tr><td>Fusion of tasks</td><td class="num"><b>89.10%</b></td><td>Joint model across outputs</td></tr>
        <tr><td>On-device cost</td><td class="num"><b>22 MB</b> · <b>0.78 s</b></td><td>Runs on a Raspberry Pi, no cloud needed</td></tr>
      </tbody>
    </table>
  </div>
  <p class="figcap" style="text-align:left">All numbers are from controlled lab studies in the author’s doctoral thesis. Real homes are harder; see limits below.</p>
</div></section>

<section class="section gray"><div class="wrap split">
  <div class="reveal">
    <span class="kicker">PUBLISHED WORK</span>
    <h2 class="h2" style="margin-top:12px">Peer-reviewed foundations.</h2>
    <p class="lead" style="margin-top:16px">The methods behind Happy Steps are published in five journals and five conferences, with four patents.</p>
    <ul class="checks">
      <li><span><b>IEEE Transactions on Mobile Computing</b></span></li>
      <li><span><b>Scientific Data</b> (Nature portfolio) · the VIBeID dataset</span></li>
      <li><span><b>IEEE Signal Processing Letters</b></span></li>
      <li><span><b>IEEE Sensors Journal</b></span></li>
      <li><span><b>IEEE Transactions on Instrumentation and Measurement</b></span></li>
    </ul>
  </div>
  <div class="card reveal" id="limits">
    <div class="icon-chip yellow">""" + ic("flask") + """</div>
    <h3>Honest limits</h3>
    <ul style="margin:14px 0 0;padding-left:18px;color:var(--muted);display:grid;gap:8px">
      <li>Each new floor needs a short setup walk to learn how it rings.</li>
      <li>Two people walking at once is harder; we tag those walks as mixed.</li>
      <li>Lab results will drop in busy homes with washing machines and pets. A home pilot is the next step.</li>
      <li>It is a care helper, not a medical device. It describes change; it never diagnoses.</li>
    </ul>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="kicker">RESEARCH ROADMAP</span><h2 class="h2">What we are building next.</h2></div>
  <div class="road" style="margin-top:48px">
    <div class="card reveal"><div class="when">Vision → vibration</div><h3>Synthetic footsteps</h3><ul><li>Generate floor signals from video of walking</li><li>Like text-to-speech, but for footsteps</li><li>New floors without new recordings</li></ul></div>
    <div class="card reveal"><div class="when">On device</div><h3>Smaller, local reasoning</h3><ul><li>TinyML step models on microcontrollers</li><li>Explore on-device Gemini Nano for offline notes</li><li>Lower cost per room</li></ul></div>
    <div class="card reveal"><div class="when">Across days</div><h3>Longer memory</h3><ul><li>Months of baseline, seasonal patterns</li><li>Early, gentle trend reports for families</li><li>Studies with care professionals</li></ul></div>
  </div>
</div></section>
""" + CTA

# ======================================================================
PRIV = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow green">""" + ic("shield", 'width="16" height="16"') + """ Privacy &amp; safety</span>
  <h1 class="h1">Private by physics. Careful by design.</h1>
  <p class="lead">A floor sensor cannot see a face or hear a word. On top of that, Happy Steps keeps the signal at home and sends only what is needed to care.</p>
  <p class="ja">見ない、聞かない、送りすぎない。</p>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="grid g3">
    <div class="card reveal"><div class="icon-chip green">""" + ic("eyeoff") + """</div><h3>Nothing to see or hear</h3><p>A geophone measures floor motion only. There is no image, no audio, and no way to rebuild speech from it.</p></div>
    <div class="card reveal"><div class="icon-chip">""" + ic("home") + """</div><h3>The signal stays home</h3><p>All signal processing runs on the device in the home. Raw vibration is never uploaded.</p></div>
    <div class="card reveal"><div class="icon-chip yellow">""" + ic("lock") + """</div><h3>Only small numbers leave</h3><p>About 300 bytes per walk: time, steps, pace, steadiness, and “resident” or “unknown”. No names in the event.</p></div>
  </div>
</div></section>

<section class="section gray"><div class="wrap split">
  <div class="reveal">
    <span class="kicker">WHAT GEMINI SEES</span>
    <h2 class="h2" style="margin-top:12px">Exactly this, and nothing more.</h2>
    <ul class="checks">
      <li><span>Today’s walk events, in the open <code>footstep-event/v1</code> format</span></li>
      <li><span>A 14-day summary of the resident’s own usual days</span></li>
      <li><span>How the family calls her (for example “お母さん”), chosen by the family</span></li>
      <li><span>A system instruction that forbids diagnosis and asks for kind, simple words</span></li>
    </ul>
  </div>
  <div class="table-wrap reveal">
    <table class="t">
      <thead><tr><th>Data</th><th>Where it lives</th></tr></thead>
      <tbody>
        <tr><td>Raw floor vibration</td><td><span class="pill green">Home device only</span></td></tr>
        <tr><td>Footstep fingerprint of the resident</td><td><span class="pill green">Home device only</span></td></tr>
        <tr><td>Walk events (numbers)</td><td><span class="pill blue">Sent to Gemini API</span></td></tr>
        <tr><td>Family note and alerts</td><td><span class="pill blue">Family’s chosen app</span></td></tr>
        <tr><td>Images, audio, location</td><td><span class="pill gray">Never collected</span></td></tr>
      </tbody>
    </table>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="kicker">SAFETY PRINCIPLES</span><h2 class="h2">Care that knows its limits.</h2></div>
  <div class="grid g2" style="margin-top:48px">
    <div class="card reveal"><h3>Consent first</h3><p>The person living in the home agrees to the sensor, can pause it, and can ask for it to be removed at any time. The family sees summaries, not a live feed.</p></div>
    <div class="card reveal"><h3>No diagnosis</h3><p>Happy Steps describes changes (“slower than usual”) and suggests human actions (“give her a call”). It never names a disease or gives medical advice.</p></div>
    <div class="card reveal"><h3>A human decides</h3><p>Alerts ask a person to check. Nothing happens automatically to the resident. Emergency services are a human choice.</p></div>
    <div class="card reveal"><h3>Kind words, always</h3><p>Messages spoken to the resident are short and cheerful. Worry goes to the family, not to her.</p></div>
  </div>
  <div class="note reveal" style="margin-top:32px"><b>About the live demo:</b> if you paste a Gemini API key, it stays in your browser and is sent only to Google’s Gemini API. The page has no server of its own. The demo uses lab recordings from consenting adult participants, with no names attached.</div>
</div></section>
""" + CTA

# ======================================================================
ABOUT = """
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">About</span>
  <h1 class="h1">I live far from my own family. So I know the worry.</h1>
  <p class="lead">Happy Steps began as a PhD on reading people from floor vibrations. Moving to Tokyo, I saw how many parents live alone, and how much their families want a gentle way to know they are okay.</p>
</div></section>

<section class="section tight"><div class="wrap split wide-l">
  <div class="reveal">
    <span class="kicker">FOUNDER</span>
    <h2 class="h2" style="margin-top:12px">Mainak Chakraborty</h2>
    <p class="lead" style="margin-top:16px">Researcher in structural vibration sensing and human-centred AI. PhD in Cyber-Physical Systems from IIT Delhi as a Prime Minister’s Research Fellow, now based in Tokyo.</p>
    <ul class="checks">
      <li><span>Creator of <b>VIBeID</b>, a 100-person footstep vibration dataset</span></li>
      <li><span><b>5 journal papers</b>, 5 conference papers and <b>4 patents</b> in vibration sensing</span></li>
      <li><span>Reviewer for IEEE TIM and IEEE TMC; ICASSP 2025 organising committee</span></li>
      <li><span>Poster presenter at the Heidelberg Laureate Forum 2026</span></li>
      <li><span>Also built <b>GajGamini</b>, ground-vibration sensing for elephant safety</span></li>
    </ul>
    <p style="margin-top:28px"><a class="btn btn-outline" href="https://mainakchakraborty.com">mainakchakraborty.com """ + ic("arrow") + """</a></p>
  </div>
  <div class="card reveal" style="background:linear-gradient(160deg,var(--blue-50),var(--green-50));border:0;padding:40px">
    <div class="icon-chip" style="background:#fff">""" + ic("heart") + """</div>
    <h3 style="font-size:1.5rem;font-weight:400;line-height:1.35">“I want a family to know grandma is okay, without anyone watching her.”</h3>
    <p class="ja" style="margin-top:14px;font-size:1rem">「見張るのではなく、そっと見守りたい。」</p>
  </div>
</div></section>

<section class="section gray"><div class="wrap">
  <div class="section-head reveal"><span class="kicker">ROADMAP</span><h2 class="h2">Where Happy Steps is going.</h2></div>
  <div class="road" style="margin-top:48px">
    <div class="card reveal"><div class="when">Now · 2026</div><h3>Working prototype</h3><ul><li>Full pipeline on real recordings</li><li>Gemini reasoning, function calling, voice</li><li>Open event format and sensor bridge</li></ul></div>
    <div class="card reveal"><div class="when">Next</div><h3>Home pilot in Japan</h3><ul><li>A small group of volunteer homes</li><li>Real floors, real routines, real feedback</li><li>Measure false alarms and family trust</li></ul></div>
    <div class="card reveal"><div class="when">Later</div><h3>Care homes and cities</h3><ul><li>Night rounds in care homes</li><li>Hospital recovery wards</li><li>Earthquake response: who is still inside</li></ul></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="kicker">WHAT WE ARE LOOKING FOR</span><h2 class="h2">Partners who care about the same thing.</h2></div>
  <div class="grid g3" style="margin-top:48px">
    <div class="card reveal"><div class="icon-chip">""" + ic("flask") + """</div><h3>Research partners</h3><p>Multimodal and on-device AI, audio and signal modelling, and long-term health reasoning.</p></div>
    <div class="card reveal"><div class="icon-chip green">""" + ic("home") + """</div><h3>Pilot homes</h3><p>Families and care homes in Japan willing to try a sensor and share honest feedback.</p></div>
    <div class="card reveal"><div class="icon-chip yellow">""" + ic("people") + """</div><h3>Care professionals</h3><p>Nurses, carers and geriatric doctors to shape what “a change worth telling” really means.</p></div>
  </div>
</div></section>
""" + CTA

# ======================================================================
DEMO_HEAD = '<link rel="stylesheet" href="assets/demo.css">'
DEMO = open(__file__.replace("pages.py", "demo_body.html"), encoding="utf-8").read()

PAGES = [
    dict(file="index.html", title="Happy Steps — every step says “I’m okay”",
         desc="Camera-free care. A floor sensor feels footsteps, a home device turns them into a tiny summary, and Gemini writes a kind daily note for the family.",
         body=INDEX, scripts='<script src="assets/hero-data.js"></script>'),
    dict(file="how-it-works.html", title="How it works — Happy Steps",
         desc="Sense, understand at the edge, summarise, reason with Gemini, and speak. The architecture of Happy Steps.", body=HOW),
    dict(file="technology.html", title="Technology — Happy Steps",
         desc="The physics, pipeline and published results behind Happy Steps floor-vibration sensing.", body=TECH),
    dict(file="demo.html", title="Live demo — Happy Steps",
         desc="Run real floor recordings through the Happy Steps pipeline and call Gemini in your browser.",
         body=DEMO, head=DEMO_HEAD, scripts='<script src="data/walkers.js"></script>\n<script src="assets/demo.js"></script>'),
    dict(file="privacy.html", title="Privacy & safety — Happy Steps",
         desc="Private by physics: no images, no audio, and the raw signal never leaves the home.", body=PRIV),
    dict(file="about.html", title="About — Happy Steps",
         desc="Founder story, roadmap and partners for Happy Steps.", body=ABOUT),
]
