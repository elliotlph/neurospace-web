"""Generates the static Neurospace site into /home/claude/neurospace-site."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "site"
EMAIL = "elliot@neurospacecoaching.com"
SITE = "https://neurospacecoaching.com"
HOURS = "Monday–Thursday, 2pm–9pm CET"
BOOK = "https://calendly.com/elliot_lphelt/free-consultation"
FORM_ENDPOINT = "https://formspree.io/f/xdegzbpl"
ADDRESS = "Mareschstraße 10<br>12055 Berlin<br>Deutschland / Germany"

GHOST = """<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M32 6c-12.2 0-21 9.4-21 21.5V55c0 1.6 1.8 2.5 3.1 1.5l4.4-3.3 4.6 3.6c.8.6 1.9.6 2.6 0L30 53.3l4.3 3.5c.8.6 1.9.6 2.6 0l4.6-3.6 4.4 3.3c1.3 1 3.1.1 3.1-1.5V27.5C53 15.4 44.2 6 32 6z" fill="#fff" stroke="#16171B" stroke-width="3" stroke-linejoin="round"/><circle cx="25" cy="28" r="3.2" fill="#16171B"/><circle cx="39" cy="28" r="3.2" fill="#16171B"/><path d="M27 36c2.8 2.6 7.2 2.6 10 0" fill="none" stroke="#16171B" stroke-width="3" stroke-linecap="round"/><circle cx="20" cy="34" r="2.6" fill="#27B6F8" opacity=".55"/><circle cx="44" cy="34" r="2.6" fill="#27B6F8" opacity=".55"/></svg>"""

NAV = [("about.html", "About"), ("services.html", "Services"), ("approach.html", "Approach"),
       ("sliding-scale.html", "Sliding Scale")]


def img(name, alt, cls="photo"):
    return (f'<div class="{cls}"><img src="assets/img/{name}" alt="{alt}" loading="lazy" '
            f'onerror="this.style.display=\'none\'"></div>')


def page(file, title, desc, body, current=None):
    path = "/" if file == "index.html" else "/" + file.removesuffix(".html")
    canon = "" if file == "404.html" else (f'<link rel="canonical" href="{SITE}{path}">\n<meta property="og:url" content="{SITE}{path}">')
    links = "".join(
        f'<a href="{h}"{" aria-current=page" if h == current else ""}>{t}</a>' for h, t in NAV)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://neurospacecoaching.com/assets/img/logo-social.png">
{canon}
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="preload" href="assets/fonts/titan-one-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head" id="top">
  <div class="wrap head-row">
    <a class="brand" href="index.html"><img class="ghost-lt" src="assets/img/ghost-mark.webp" alt="" width="210" height="370"><span>Neurospace</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn" href="contact.html"{" aria-current=page" if current == "contact.html" else ""}>Get started</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="brand" href="index.html"><img src="assets/img/ghost-mark-light.webp" alt="" width="210" height="370"><span>Neurospace Coaching</span></a>
        <p>Radical coaching for weirdos. Queer and neurodivergent centered, based in Berlin, working virtually in English.</p>
      </div>
      <div>
        <h3>Explore</h3>
        <ul><li><a href="about.html">About</a></li><li><a href="index.html#meet-elliot">Meet Elliot</a></li><li><a href="services.html">Services</a></li><li><a href="approach.html">Approach</a></li><li><a href="sliding-scale.html">Sliding Scale</a></li><li><a href="contact.html">Contact</a></li></ul>
      </div>
      <div>
        <h3>Hours</h3>
        <p>{HOURS}</p>
        <h3>Email</h3>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </div>
    <div class="foot-base">
      <span>© 2026 Neurospace Coaching</span>
      <span><a href="privacy-policy.html">Privacy Policy</a> · <a href="impressum.html">Impressum</a></span>
    </div>
  </div>
</footer>
<script>
const b=document.querySelector('.menu-btn'),n=document.getElementById('nav');
b.addEventListener('click',()=>{{const o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)}});
const h=document.querySelector('.site-head');addEventListener('scroll',()=>h.classList.toggle('scrolled',scrollY>8),{{passive:true}});
</script>
</body>
</html>
"""
    (OUT / file).write_text(html)


CTA = f"""<div class="wrap cta-wrap"><div class="cta">
  <div>
    <span class="eyebrow">Virtual Coaching Sessions</span>
    <h2>Ready to start?</h2>
    <p>Reach out to schedule a consultation!<br><a class="mail" href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p style="margin-top:22px"><a class="btn ghost-btn" href="{BOOK}" target="_blank" rel="noopener">Book a free consultation ↗</a></p>
  </div>
  <div class="ghost-art float"><img src="assets/img/ghost-mark-light.webp" alt=""></div>
</div></div>"""

VALUES = """<div class="cards values">
  <div class="card"><h3>Authenticity</h3><p>Okay, I know this word can sound corny or over-done but I really do believe that when we can access our most genuine self, we are able to experience life in a much richer color. And when I say authentic, I don’t mean not giving a f*ck about what other people think, I just mean being as true to yourself as possible in any given moment.</p></div>
  <div class="card"><h3>Agency</h3><p>I use this word a lot because it’s at the core of what I believe causes suffering: a lack or stripping away of agency. When we don’t feel like active and consenting participants in our lives, we experience immense emotional and mental distress. By my logic, reclaiming agency is key to growth.</p></div>
  <div class="card"><h3>Autonomy</h3><p>Similar but different than agency, it’s imperative in my opinion, that we foster access to our own autonomy. Not in the sense of individualism, but rather the experience of being a differentiated but interdependent self that coexists with others. When we feel autonomous, we actually have more capacity for connection and a felt sense of safety.</p></div>
</div>"""


def card(title, text):
    return f'<div class="card"><h3>{title}</h3><p>{text}</p></div>'


# ---------- HOME ----------
page("index.html",
     "Neurospace Coaching | Queer & Neurodivergent Coach and Couples Counsellor — Berlin, Germany",
     "Virtual life coaching and couples counselling for queer, neurodivergent and non-monogamous people. Based in Berlin, working in English across Europe, North America and beyond.",
     f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">Coaching &amp; counselling</span>
    <h1>This is for the <mark>weirdos</mark></h1>
    <p class="lead">Stop living for others and start dealing with the real sh*t</p>
      </div>
  <div class="blob"><span class="sticker s1">Berlin +<br>virtual</span><a class="sticker s2" href="{BOOK}" target="_blank" rel="noopener" style="text-decoration:none;color:var(--ink)">Free<br>consult!</a>{img("ghost-costume.webp", "A person dressed as a ghost with white fabric and glasses, standing outdoors under a blue sky with clouds.", "frame")}</div>
</div>
<div class="pill-row"><ul class="pills" aria-label="Who this is for"><li class="pill ghost">Queer</li><li class="pill lime">Neurodivergent</li><li class="pill pink">Non-monogamous</li><li class="pill lilac">Couples &amp; polycules</li><li class="pill teal">No pathologizing</li><li class="pill lime">Real talk</li><li aria-hidden="true" class="pill ghost">Queer</li><li aria-hidden="true" class="pill lime">Neurodivergent</li><li aria-hidden="true" class="pill pink">Non-monogamous</li><li aria-hidden="true" class="pill lilac">Couples &amp; polycules</li><li aria-hidden="true" class="pill teal">No pathologizing</li><li aria-hidden="true" class="pill lime">Real talk</li></ul><ul class="pills" aria-hidden="true"><li class="pill ghost">Queer</li><li class="pill lime">Neurodivergent</li><li class="pill pink">Non-monogamous</li><li class="pill lilac">Couples &amp; polycules</li><li class="pill teal">No pathologizing</li><li class="pill lime">Real talk</li><li class="pill ghost">Queer</li><li class="pill lime">Neurodivergent</li><li class="pill pink">Non-monogamous</li><li class="pill lilac">Couples &amp; polycules</li><li class="pill teal">No pathologizing</li><li class="pill lime">Real talk</li></ul></div>
</section>

<section class="band"><div class="wrap split">
  <div><span class="eyebrow">About Neurospace</span><h2>Don't worry, we're all weird here.</h2></div>
  <div class="prose">
    <p>I built Neurospace Coaching because I was done watching people fall through the cracks of a system that wasn't built for them — and honestly, because I needed something different too.</p>
    <p>My background is clinical. Five years as a therapist, a Master's degree, the whole thing. But what I do now isn't therapy, it's more direct, more collaborative, and a lot less interested in keeping you comfortable with the status quo. If conventional approaches haven't been cutting it, that's not a you problem.</p>
    <p>What coaching with me actually looks like: someone willing to get in the mess with you and then help you figure out what to do about it. We'll look at what's keeping you stuck, get clear on what you actually want, and build toward that— whether that's who you are, how you're showing up in your relationships, or just how you want to be living your life.</p>
  </div>
</div></section>

<section id="meet-elliot"><div class="wrap split">
  {img("elliot-home.webp", "Elliot, founder of Neurospace Coaching")}
  <div class="prose">
    <span class="eyebrow">Meet Elliot</span>
    <h2>Curious, passionate, and <mark>realistic</mark></h2>
    <p>Curious, passionate, and realistic— that's how I'd describe myself and my approach.</p>
    <p>Curiosity is non-negotiable. Nothing changes without a willingness to ask hard questions and actually look at the answers. I've seen firsthand what happens when people lead with it: they learn, they shift, they evolve. That's what coaching is for.</p>
    <p>I do this work because I genuinely care about emotional health and human connection. I want you to be the cool ass person you are and live accordingly. If I get to play a role in that, I'm grateful.</p>
    <p>The realist in me means I'm not just here to talk things through, I'm here to help you turn what you're thinking and hoping into actual movement. I won't pretend this is easy or that the world isn't on fire. But I will challenge you to think and do differently, while being a space where your real feelings can land without judgment.</p>
    <p>I believe in your right to joy, pleasure, and connection. Let's build more of that.</p>
    <p>I'm based in Berlin and work virtually with clients across Europe, North America, and beyond providing English-speaking coaching and counselling, {HOURS}.</p>
    <a class="btn" href="contact.html">Get started</a>
  </div>
</div></section>

<section class="band lime"><div class="wrap">
  <span class="eyebrow">What I work with</span>
  <h2>Figuring out what's not working, and building something better</h2>
  <p class="intro">Whether you'd call it coaching or counselling, what we're doing together is figuring out what's not working and building something better. I work with:</p>
  <div class="cards">
    {card("Identity and self-exploration", "Who you are, who you want to be, and what's been getting in the way")}
    {card("Relationship coaching and counselling", "Couples, partners, and polycules navigating communication, conflict, and connection")}
    {card("Non-monogamy and ethical non-monogamy (ENM)", "Whether you're new to it or untangling years of patterns")}
    {card("Neurodivergence", "ADHD, autism, and more. Everything that comes with navigating a world that wasn't designed for your brain")}
    {card("Life transitions and burnout", "Career pivots, relocations, identity shifts, starting over")}
    {card("Immigrant, Expat, and cross-cultural stress", "Whether you’re in a cross-cultural relationship (I am) or navigating life as an immigrant in a new country, I see you")}
  </div>
  <p style="margin-top:32px">If you're not sure whether what I do is a fit for what you need, that's exactly what a free consultation is for.</p>
</div></section>

<section><div class="wrap">
  <span class="eyebrow">My Coaching Values</span>
  <h2>Authenticity, agency, autonomy</h2>
  {VALUES}
</div></section>
{CTA}
""")

# ---------- ABOUT ----------
page("about.html", "About | Neurospace Coaching",
     "Queer and neurodivergent centered coaching with Elliot (they/she), a former therapist based in Berlin.",
     f"""
<section class="page-hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">About</span>
    <h1>It’s 2026, we’re dropping the <mark>mask</mark></h1>
    <p class="lead">The world is objectively exhausting and terrifying right now and you deserve a space for yourself to decompress and be real.</p>
  </div>
  <div class="blob">{img("couple.webp", "Two women with different skin tones and curly hair lying on a bed, kissing each other.", "frame")}</div>
</div></section>

<section class="band pink"><div class="wrap split">
  <div><span class="eyebrow">Queer &amp; Neurodivergent Centered</span><h2>Here, you get to just be you</h2></div>
  <div class="prose">
    <p>A lot of people are using the word “affirming” and while it’s great to see overall, I think we’re getting lost in the sauce and the term is over-saturated.</p>
    <p>In my coaching practice I’m all about those of us who are called freaks, weirdos, and outsiders. Although I have come to a place where I can now embrace and celebrate who I am (most days), it doesn’t mean those words don’t still carry weight.</p>
    <p>But here, you get to release that burden and just be you. And from there, be the version of yourself you have been working towards for years. Things are tough. I am here to make it a bit easier for you so that the good days get longer and the bad days pass easier.</p>
    <a class="btn" href="contact.html">Get started</a>
  </div>
</div></section>

<section><div class="wrap split">
  {img("elliot-about.webp", "Elliot, founder of Neurospace Coaching")}
  <div class="prose">
    <span class="eyebrow">Meet Elliot</span>
    <h2>Hi y'all, I'm Elliot (they/she)</h2>
    <p>I switched to coaching in 2025 after years as a therapist and the short version of why is that I got tired of watching a broken system harm the people it's supposed to help. Licensure requirements don't protect clients from bad therapists, restrictions make it hard to find competent providers, and clinicians are overworked, devalued, and underpaid. I could go on. I won't.</p>
    <p>What I never got tired of was the actual work— being in the room when something shifts, watching someone's life gain more ease or clarity. That’s why I do this.</p>
    <p>My clinical background gives me real insight into emotional patterns and human behavior, but coaching lets me work differently. The focus isn't on what's "wrong" with you, it's on who you want to become and what's getting in the way. I'm not here to treat mental health conditions. I'm here to help you figure out your shit and make moves.</p>
    <p>That looks different for everyone:</p>
    <ul class="checks">
      <li>Deconstructing societal oppression to explore your realest self? Check.</li>
      <li>Burnt out and looking for something new? Check.</li>
      <li>Navigating relationship strain and want to actually communicate better? Check.</li>
    </ul>
    <p>I'm good at this because I've been through some shit too. When I say I can help you navigate stress and grow, it's because I'm doing it myself.</p>
    <p>I relocated to Berlin in 2026 and work virtually with clients throughout Germany, the EU, and beyond.</p>
    <a class="btn ghost-btn" href="contact.html">Let's connect</a>
  </div>
</div></section>

<section class="band lilac"><div class="wrap split">
  <div><span class="eyebrow">Training &amp; Education</span><h2>Where the work comes from</h2></div>
  <div class="timeline prose">
    <div class="item"><h3>Neurodivergent Somatics</h3><p>A cohort live learning lab provided by Nyck Walsh, MA, LPC completed in March 2024.</p><p>Created to go deeper into how to effectively engage in anti-ableist somatic approaches with Neurodivergent clients (continued focus on Autism and ADH/ADHD). Principles of learning include: Concrete somatic tools and strategies for nervous system regulation; Practices for dismantling internalized ableism/ableism; Boundaries as a much needed form of differentiation in support of empowerment, clarity, and unmasking; Accommodations and executive function supports that are needed for the everyday and to prevent provider burn-out.</p></div>
    <div class="item"><h3>Somatics with Queer &amp; Trans Clients</h3><p>Provided by Andrea Guitierez-Glik, LMSW. Completed Dec '20. Training in the use of somatic (body-based) modalities attuned specifically to working with queer and trans clients.</p></div>
    <div class="item"><h3>Integrated Somatic Trauma Certificate</h3><p>Provided through Embody Lab with instruction from leaders in the field of trauma-informed somatic providers including Stacy Haines, Richard Schwartz, Euphrasia "Efu" Nyaki, Peter Levine, Arielle Schwartz, Pat Ogden, Ruby Gibson, and others. Fall 2022.</p></div>
    <div class="item"><h3>Somatic Parts Work</h3><p>Provided by Fran Booth. Completed Sept ‘22. Integration of somatic work and internal family systems.</p></div>
    <div class="item"><h3>MA Marriage and Family Therapy</h3><p>I received my Master’s in Marriage and Family Therapy in December 2021.</p></div>
  </div>
</div></section>
{CTA}
""", "about.html")

# ---------- SERVICES ----------
page("services.html", "Services | Neurospace Coaching",
     "Individual, relationship and polycule coaching for queer, neurodivergent and non-monogamous people.",
     f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Services</span>
  <h1>Ways we can <mark>work</mark> together</h1>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="cards">
    <div class="card"><h3>Individual Coaching</h3><p>Individual coaching is one-on-one work for people who feel stuck, overwhelmed, or like something just isn't working. We'll look at what's actually going on—the patterns keeping you where you are, the stuff you're carrying from the past, the gap between who you are and how you're living. Then we'll figure out what to do about it. You'll leave with real tools and a clearer sense of yourself.</p><p><a href="sliding-scale.html">Reduced Rate Info</a></p></div>
    <div class="card"><h3>Relationship Coaching</h3><p>Partner coaching is where we figure out why you keep having the same fights and what's actually underneath them. We'll look at your patterns and how you communicate (or don't), what you're really needing from each other, and what old stuff is bleeding into the present. Then we'll work on practical ways to talk to each other, handle conflict, and stop letting the same issues take you down.</p><p><a href="sliding-scale.html">Reduced Rate Info</a></p></div>
    <div class="card"><h3>Polycule Relationship Coaching</h3><p>Polycule coaching is group work for multi-partner relationships that need help with the complicated stuff, communication breakdowns, conflicting needs, unclear boundaries, or just figuring out how to make it all work. We'll tackle the dynamics that are causing friction and build practical skills for navigating conflict, setting boundaries, and actually showing up for each other. Whether you're new to this or trying to untangle years of patterns, this is where you work on it together.</p><p><a href="sliding-scale.html">Reduced Rate Info</a></p></div>
  </div>
  <p style="margin-top:32px"><a class="btn" href="contact.html">Get started</a></p>
</div></section>

<section class="band lilac"><div class="wrap split flip">
  <div class="prose">
    <span class="eyebrow">Why Coaching?</span>
    <h2>Why Coaching?</h2>
    <p>Let’s talk about if coaching might be a good, or better, fit for you and what to actually expect to gain from this work together.</p>
    <h3>First, what’s the difference between coaching and therapy?</h3>
    <p>These aren't totally separate worlds, and I won't pretend they are. My clinical background means I understand emotional patterns, relationship dynamics, and the specific weight that queer and neurodivergent folks carry. It also means I know when someone needs more than coaching can offer. If you're in crisis, dealing with severe mental health symptoms, or need trauma processing, therapy is the right call — and I'll tell you that directly.</p>
  </div>
  {img("laughing.webp", "Two men are laughing and hugging each other, one is wearing a white t-shirt and the other is in a dark shirt.")}
</div>
<div class="wrap"><div class="cards">
  <div class="card"><h3>Therapy</h3><p>Therapy is designed to treat mental health conditions, things like depression, anxiety disorders, trauma, eating disorders, etc. It often focuses on processing past experiences, healing wounds, and managing symptoms. It's medical treatment, which is why therapists are licensed and can diagnose you.</p><p><strong>Therapy is the best option for you if:</strong></p><ul class="checks">
    <li>You're experiencing severe depression, anxiety, or other mental health symptoms that impact daily functioning</li>
    <li>You're dealing with active trauma or PTSD</li>
    <li>You're in crisis or having thoughts of self-harm</li>
    <li>You need someone who can provide clinical treatment and potentially coordinate with psychiatrists or other medical providers</li></ul></div>
  <div class="card"><h3>Coaching</h3><p>Coaching is about moving forward. We're not treating mental health conditions or diagnosing anything. Instead, we're focused on who you want to become and what you want your life to look like - whether that's figuring out your identity, navigating relationship dynamics, dealing with career burnout, or building the skills to communicate better with your partner(s).</p><p><strong>Coaching with me is right for you if:</strong></p><ul class="checks">
    <li>You're generally functioning but feel stuck or unfulfilled</li>
    <li>You want to explore your identity or values</li>
    <li>You're dealing with relationship stuff (including navigating non-monogamy)</li>
    <li>You need someone to help you figure out your next move, not just process your feelings</li>
    <li>You're tired of being pathologized and want someone who gets that being queer or neurodivergent isn't something to "fix"</li></ul></div>
</div>
<p style="margin-top:32px">Still not sure? Let's talk about it in a consultation.</p>
<a class="btn ghost-btn" href="contact.html">Contact me</a>
</div></section>

<section><div class="wrap split">
  {img("services-2.webp", "")}
  <div class="prose">
    <span class="eyebrow">What to expect</span>
    <h2>What to expect</h2>
    <p>Neither coaching or therapy change your life in an instant and I will never imply or promise that outcome to clients. Coaching is a real investment in yourself, your relationships, and where you're headed. Change takes effort and intentionality. My job is to help you figure out what needs to shift, and reinforce what's already working, so you feel clearer and more capable of actually moving.</p>
    <p>This is about reclaiming agency. We'll use your core values as a compass and build toward goals you actually care about so that even on the bad days, you have something to orient toward. A session might look like mapping out the next few months to get your work-life balance under control, unpacking a conflict pattern that keeps blowing up your relationship, or literally figuring out how to do the dishes when your executive functioning has left the building.</p>
    <p>This isn't just venting. We'll talk through your feelings, absolutely, but the goal is always movement. I'll challenge you, ask uncomfortable questions, and hold you to the changes you say you want to make. I'm supportive as hell, but I'm not here to validate everything you do (unlike ChatGPT).</p>
    <p>A lot of people come to me having felt stuck in therapy. It usually comes down to the same few things: expecting change to be fast, avoiding the real shit, and having no actual plan for moving forward. Coaching is structured differently. We're not just processing, we're building.</p>
    <p>If you're ready to break old patterns and get to what's actually holding you back, let's do it.</p>
  </div>
</div></section>
{CTA}
""", "services.html")

# ---------- APPROACH ----------
page("approach.html", "My Coaching Approach | Neurospace Coaching",
     "Evidence-based, intuitive and creative coaching built on authenticity, agency and autonomy.",
     f"""
<section class="page-hero"><div class="wrap">
  <div class="prose">
    <span class="eyebrow">Approach</span>
    <h1>My Coaching <mark>Approach</mark></h1>
    <p class="lead">I see myself as someone who stands alongside people through the real complexity of life— not above it, not outside it.</p>
    <p>My approach is evidence-based, intuitive, and creative. I think of coaching as a kind of alchemy: multiple things have to come together to create genuine change. For me, those are authenticity, agency, and autonomy. Whatever you're bringing to this work, those three things are the foundation.</p>
    <p>Let's talk and see where it goes.</p>
    <a class="btn" href="contact.html">Let's talk</a>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <span class="eyebrow">The foundation</span>
  <h2>So what’s this all about?</h2>
  {VALUES}
</div></section>

<section><div class="wrap">
  <div class="split flip" style="align-items:center">
    <div><span class="eyebrow">Focus areas</span><h2>What can coaching help with?</h2></div>
    {img("graffiti.webp", "", "photo wide")}
  </div>
  <div class="cards">
    {card("Gender identity exploration", "Whether you're just getting curious or deep in transition, I get it from both professional and personal experience.")}
    {card("Neurodivergence", "Especially ADHD and autism. Figuring out your neurotype and what that means for how you move through the world.")}
    {card("Nonmonogamous Relationships", "Polyamory, mono-poly dynamics, queer platonic partnerships, or anything outside the standard script.")}
    {card("Future Anxiety", "The world is a lot right now. We'll work on staying grounded in the present without losing hope.")}
    {card("Self-Worth", "Rebuilding what's been chipped away, because you deserve to feel solid in who you are.")}
    {card("Work Stress", "Figuring out how to find work that doesn't destroy you, advocating for yourself, or navigating being queer/neurodivergent in professional spaces.")}
  </div>
</div></section>
{CTA}
""", "approach.html")

# ---------- SLIDING SCALE ----------
page("sliding-scale.html", "Fee Structure & Cost | Neurospace Coaching",
     "Sliding-scale session fees based on client-reported income, for clients in the US, UK and EU.",
     f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Sliding Scale</span>
  <h1>Fee Structure &amp; <mark>Cost</mark></h1>
  <p class="lead">Session cost operates based on a sliding scale structure determined by client-reported income.</p>
  <div class="price-grid">
    <div class="price"><span class="tag">Bracket A</span><h3>Constrained</h3><p>Enough to cover essentials, utilities, and basic bills. Savings are minimal or non-existent. Prioritizing needs over wants.</p>
      <dl><dt>Single income household</dt><dd>€100 – €125</dd><dt>Two income household</dt><dd>€115 – €130</dd></dl></div>
    <div class="price featured"><span class="tag">Bracket B</span><h3>Comfortable</h3><p>Income covers living expenses, bills, and leaves a buffer for savings or discretionary spending. Low to moderate budgeting stress.</p>
      <dl><dt>Single income household</dt><dd>€125 – €135</dd><dt>Two income household</dt><dd>€130 – €145</dd></dl></div>
    <div class="price"><span class="tag">Bracket C</span><h3>Secure</h3><p>Income exceeds living expenses. Savings and investments are a possible, allowing for lifestyle flexibility and low financial stress.</p>
      <dl><dt>Single income household</dt><dd>€140 – €155</dd><dt>Two income household</dt><dd>€150 – €160</dd></dl></div>
  </div>
</div></section>

<section style="padding-top:24px"><div class="wrap split">
  {img("sliding.webp", "")}
  <div class="prose">
    <p>The best approach is to use these ranges as a starting point rather than rigid requirements. Consider your personal situation and talk with me directly if you have questions or concerns.</p>
    <p>**I work with clients across the US, UK, and EU. Fees are adjusted accordingly to your local currency.</p>
    <h2>Questions? Reach out and let’s talk about it.</h2>
    <p style="display:flex;flex-wrap:wrap;gap:12px"><a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a free consultation ↗</a><a class="btn ghost-btn" href="contact.html">Contact me</a></p>
  </div>
</div></section>
""", "sliding-scale.html")

# ---------- CONTACT ----------
page("contact.html", "Contact | Neurospace Coaching",
     "Get in touch with Neurospace Coaching or book a free consultation.",
     f"""
<section class="page-hero"><div class="wrap hero-grid" style="align-items:start">
  <div>
    <span class="eyebrow">Contact</span>
    <h1>Let’s Get <mark>Started</mark></h1>
    <p class="lead">If you’re interested in starting coaching with me or have questions, please reach out and I will be excited to connect.</p>
    <div class="card" style="margin-top:28px">
      <h3>Radical Coaching for Weirdos</h3>
      <p><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a><br><strong>Hours:</strong> {HOURS}</p>
      <a class="btn" href="{BOOK}" target="_blank" rel="noopener">Book a free consultation ↗</a>
    </div>
  </div>
  <form class="card contact-form" id="form" action="{FORM_ENDPOINT}" method="POST" novalidate>
    <h3>Send me a message</h3>
    <p class="form-note">A short note about what you're looking for is enough. Please keep sensitive details for our free consultation.</p>
    <label>Name<input name="name" autocomplete="name" required></label>
    <label>Email<input name="email" type="email" autocomplete="email" required></label>
    <label>Message<textarea name="message" rows="5" required></textarea></label>
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" class="hp" aria-hidden="true">
    <label class="check"><input type="checkbox" name="consent" required><span>I've read the <a href="privacy-policy.html">privacy policy</a> and agree that my message is used to answer my enquiry.</span></label>
    <button class="btn" type="submit">Send message</button>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form>
</div></section>
<script>
const f=document.getElementById('form'),st=f.querySelector('.form-status');
f.addEventListener('submit',async e=>{{
  e.preventDefault();
  if(!f.checkValidity()){{st.textContent='Please fill in every field and tick the box.';f.reportValidity&&f.reportValidity();return}}
  const btn=f.querySelector('button');btn.disabled=true;st.textContent='Sending…';
  try{{
    const r=await fetch(f.action,{{method:'POST',body:new FormData(f),headers:{{Accept:'application/json'}}}});
    if(!r.ok)throw 0;
    f.reset();st.textContent='Thanks! Your message is on its way. I usually reply within a couple of working days.';
  }}catch(_){{st.innerHTML='Sorry, that didn\'t send. Please email me at <a href="mailto:{EMAIL}">{EMAIL}</a>.'}}
  btn.disabled=false;
}});
</script>
""", "contact.html")

# ---------- PRIVACY ----------
page("privacy-policy.html", "Privacy Policy | Neurospace Coaching",
     "How Neurospace Coaching collects, uses and protects personal data.",
     f"""
<section class="page-hero"><div class="wrap legal">
<h1>Privacy Policy</h1>
<p>Last updated: 19 November 2026</p>
<p>Neurospace Coaching collects only the personal data needed to run this website, answer your questions and provide coaching and counselling services. We never sell your data, and we never use it for advertising.</p>
<p>This policy explains what we collect when you visit neurospacecoaching.com, contact us or become a client, why we collect it, who helps us process it, and the rights you have. It applies to visitors and clients in the EU, the UK, the United States and anywhere else we work.</p>
<p>In this policy, "we", "us" and "our" mean Neurospace Coaching. "You" means anyone who visits the site or uses our services.</p>

<h2>1. Who is responsible for your data</h2>
<p>The controller responsible for your personal data under the EU General Data Protection Regulation (GDPR) and the UK GDPR is:</p>
<p>Elliot Lima-Pinto Helt<br>Neurospace Coaching (freelance)<br>{ADDRESS}<br>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p>We are a small practice and are not required to appoint a Data Protection Officer. For any privacy question or request, write to the email address above and Elliot will answer personally.</p>

<h2>2. What data we collect</h2>
<p>We collect data in four situations. You never have to give us more than the minimum needed for what you ask.</p>
<table><tr><th>When</th><th>What we collect</th><th>Where it comes from</th></tr>
<tr><td>You browse the site</td><td>IP address, browser and device type, page requested, date and time of visit (server logs)</td><td>Your browser, automatically</td></tr>
<tr><td>You contact us</td><td>Name, email address, your message and anything you choose to share in it</td><td>You, via email or the contact form</td></tr>
<tr><td>You book a consultation</td><td>Name, email address, chosen time and any answers you give in the booking form</td><td>You, via Calendly</td></tr>
<tr><td>You become a client</td><td>Contact details, intake and consent forms, scheduling and payment records, session notes, and information you share during sessions</td><td>You, and anyone you invite into joint sessions with your agreement</td></tr></table>
<h3>Sensitive information</h3>
<p>Coaching and counselling conversations often involve sensitive topics, such as your health, neurodivergence, sexual orientation, gender identity or relationship structure. Under GDPR these are "special categories" of data. We process them only with your explicit consent, given in your client agreement, and only to provide the services you asked for. You can withdraw that consent at any time.</p>
<p>Please don't send sensitive details in your first email. A short note about what you're looking for is enough; we can talk about the rest in your free consultation.</p>

<h2>3. How we use your data and why we're allowed to</h2>
<p>GDPR requires a legal basis for every use of personal data. Ours are:</p>
<table><tr><th>Purpose</th><th>Legal basis (GDPR / UK GDPR)</th></tr>
<tr><td>Running the website securely and keeping it working</td><td>Legitimate interest (Art. 6(1)(f))</td></tr>
<tr><td>Answering your questions and booking a consultation</td><td>Steps before a contract at your request (Art. 6(1)(b))</td></tr>
<tr><td>Providing coaching and counselling, scheduling, invoicing</td><td>Performance of a contract (Art. 6(1)(b))</td></tr>
<tr><td>Processing sensitive information shared in sessions</td><td>Your explicit consent (Art. 9(2)(a))</td></tr>
<tr><td>Keeping invoices and accounting records</td><td>Legal obligation (Art. 6(1)(c))</td></tr></table>
<p>We do not use your data for automated decision-making or profiling, and we do not send marketing emails unless you have signed up for them separately.</p>

<h2>4. Cookies</h2>
<p>This website does not set any cookies and does not use analytics, advertising, retargeting or social media tracking. Fonts are hosted on our own server, so your browser doesn't contact third-party font services when you visit.</p>

<h2>5. Who helps us process your data</h2>
<p>We share your data only with the service providers we need to run the practice. Each acts on our instructions under a data processing agreement and may not use your data for its own purposes.</p>
<table><tr><th>Provider</th><th>What they do</th><th>Location</th></tr>
<tr><td>Cloudflare</td><td>Website hosting, domain and security (server logs)</td><td>EU and USA</td></tr>
<tr><td>doxy.me</td><td>Video sessions</td><td>USA</td></tr>
<tr><td>Wise</td><td>Card and online payments</td><td>EU, UK and USA</td></tr>
<tr><td>Google Workspace</td><td>Email</td><td>EU and USA</td></tr>
<tr><td>Carepatron</td><td>Booking appointments</td><td>New Zealand, data hosted in EU</td></tr>
<tr><td>Calendly</td><td>Booking free consultations (when you follow the booking link)</td><td>USA</td></tr>
<tr><td>Formspree</td><td>Delivers messages sent through the contact form to my email</td><td>USA</td></tr>
<tr><td>Accountant / tax advisor: Annette Noll-Thissen</td><td>Bookkeeping and tax filings</td><td>Germany</td></tr></table>
<p>We also disclose data when the law requires it, for example to tax authorities.</p>
<h3>Transfers outside the EU and UK</h3>
<p>Some providers process data in the United States. Where they do, we rely on the EU–U.S. Data Privacy Framework (and its UK extension) for certified providers, or on the European Commission's Standard Contractual Clauses. You can ask us for a copy of the relevant safeguards.</p>

<h2>6. How long we keep your data</h2>
<p>We keep data only as long as we need it, then delete it securely.</p>
<table><tr><th>Data</th><th>How long</th></tr>
<tr><td>Emails and contact form messages from people who don't become clients</td><td>6 months after our last exchange</td></tr>
<tr><td>Client records, intake forms and session notes</td><td>3 years after your last session, unless you ask us to delete them sooner and no legal duty prevents it</td></tr>
<tr><td>Invoices, receipts and accounting records</td><td>8 to 10 years, as German tax and commercial law requires</td></tr>
<tr><td>Website server logs</td><td>Kept briefly by our hosting provider for security, then deleted</td></tr></table>
<p>You can ask us to delete your data earlier at any time (see section 7).</p>

<h2>7. Your rights</h2>
<p>Wherever you live, you can email <a href="mailto:{EMAIL}">{EMAIL}</a> to exercise any of these rights. We answer within one month and don't charge for it. We may ask you to confirm your identity first.</p>
<h3>If you're in the EU or UK</h3>
<p>Under the GDPR and UK GDPR you have the right to:</p>
<ul><li>Access the data we hold about you and get a copy</li><li>Correct data that is wrong or incomplete</li><li>Delete your data, unless we must keep it by law</li><li>Restrict how we use your data</li><li>Port your data to another provider in a common format</li><li>Object to processing based on our legitimate interests</li><li>Withdraw consent at any time, without affecting anything done before</li><li>Complain to a data protection authority</li></ul>
<p>Our lead authority is the Berlin Commissioner for Data Protection and Freedom of Information (datenschutz-berlin.de). UK residents can contact the Information Commissioner's Office (ico.org.uk). You can also complain to the authority where you live or work.</p>
<h3>If you're in the United States</h3>
<p>We don't sell or share your personal information for advertising, and we never have. Depending on your state, you may have the right to know what we collect, to access or delete it, to correct it, and to opt out of sale or targeted advertising. We extend these rights to all U.S. visitors and clients, and we won't treat you differently for using them.</p>

<h2>8. Security</h2>
<p>The site is served over an encrypted connection (HTTPS). Client records are kept in password-protected, access-restricted systems that only Elliot can open, and video sessions run on an encrypted platform. No system is perfectly secure, but if a breach ever puts your data at risk, we will tell you and the authorities as the law requires.</p>

<h2>9. Children</h2>
<p>Our services are for adults aged 18 and over. We don't knowingly collect data from children. If you believe a child has sent us personal data, contact us and we will delete it.</p>

<h2>10. Changes to this policy</h2>
<p>We update this policy when our services, providers or the law change. The date at the top shows the latest version. If a change significantly affects how we use client data, we will tell current clients directly.</p>

<h2>11. Contact</h2>
<p>Questions, requests or concerns about your privacy:</p>
<p>Elliot Lima-Pinto Helt · Neurospace Coaching<br>Berlin, Germany<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
</div></section>
""", "privacy-policy.html")

# ---------- IMPRESSUM ----------
page("impressum.html", "Impressum | Neurospace Coaching", "Legal notice (Impressum) for Neurospace Coaching.",
     f"""
<section class="page-hero"><div class="wrap legal">
<h1>Impressum</h1>
<p><em>English version below.</em></p>

<h2>Angaben gemäß § 5 DDG</h2>
<p>Elliot Lima-Pinto Helt<br>Neurospace Coaching<br>Freiberufliche Tätigkeit<br>{ADDRESS}</p>

<h2>Kontakt</h2>
<p>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Kontaktformular: <a href="contact.html#form">neurospacecoaching.com/contact</a></p>

<h2>Berufsbezeichnung</h2>
<p>Coach. Coaching ist in Deutschland kein reglementierter Beruf; es gelten keine besonderen berufsrechtlichen Regelungen und keine Kammerzugehörigkeit. Coaching ist keine Psychotherapie und keine Heilbehandlung.</p>

<h2>Verbraucherstreitbeilegung</h2>
<p>Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen. Beschwerden können Sie jederzeit an <a href="mailto:{EMAIL}">{EMAIL}</a> richten.</p>

<h2>Haftung für Links</h2>
<p>Diese Website enthält Links zu externen Websites Dritter, auf deren Inhalte ich keinen Einfluss habe. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter verantwortlich. Bei Bekanntwerden von Rechtsverletzungen entferne ich derartige Links umgehend.</p>

<hr style="border:0;border-top:3px solid var(--ink);margin:3em 0">

<h2>Legal notice (English)</h2>
<p>Information pursuant to § 5 of the German Digital Services Act (DDG):</p>
<p>Elliot Lima-Pinto Helt<br>Neurospace Coaching<br>Self-employed (freelance)<br>{ADDRESS}</p>
<p><strong>Contact:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="contact.html#form">contact form</a></p>
<p><strong>Professional title:</strong> Coach. Coaching is not a regulated profession in Germany; no professional chamber or special professional rules apply. Coaching is not psychotherapy or medical treatment.</p>
<p><strong>Consumer dispute resolution:</strong> I am neither willing nor obliged to take part in dispute resolution proceedings before a consumer arbitration board. You can send complaints to <a href="mailto:{EMAIL}">{EMAIL}</a> at any time.</p>
<p><strong>Links:</strong> This site links to external websites whose content I don't control. The provider of each linked site is responsible for its content. I'll remove any link promptly if I become aware that it infringes the law.</p>
</div></section>
""")

# ---------- 404 ----------
page("404.html", "Page not found | Neurospace Coaching", "Page not found.",
     f"""
<section class="page-hero"><div class="wrap" style="text-align:center">
  <div class="float" style="width:110px;margin:0 auto 24px"><img src="assets/img/ghost-mark.webp" alt=""></div>
  <h1><mark>Boo.</mark> Nothing here.</h1>
  <p class="lead" style="margin:0 auto 28px">This page has vanished. Let's get you somewhere real.</p>
  <a class="btn" href="index.html">Back home</a>
</div></section>
""")

print("built", sorted(p.name for p in OUT.glob("*.html")))


# ---------- SITEMAP + ROBOTS ----------
import datetime
TODAY = datetime.date.today().isoformat()
pages = ["index.html", "about.html", "services.html", "approach.html", "sliding-scale.html",
         "contact.html", "privacy-policy.html", "impressum.html"]
urls = "".join(
    f"  <url><loc>{SITE}{'/' if f == 'index.html' else '/' + f.removesuffix('.html')}</loc><lastmod>{TODAY}</lastmod></url>\n"
    for f in pages)
(OUT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
print("sitemap + robots written")
