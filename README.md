# hotseat-mediator

**[▶ Try it online](https://dvelton.github.io/hotseat-mediator/)**

A structured settlement negotiation tool that helps two parties find common ground — without losing bargaining position.

## The Problem

In real-world litigation, countless cases fail to settle as quickly as they should because of a fundamental rule of negotiation: both sides must maintain bargaining position.

A Plaintiff willing to accept $50,000 can't say so — the Defendant would treat it as a ceiling and negotiate down. A Defendant willing to pay $50,000 can't say so either — the Plaintiff would treat it as a floor and push higher. Both sides posture with artificial numbers, creating an impasse that can take months or years to break through.

## How It Works

Hotseat Mediator creates **information asymmetry** that breaks through the impasse:

1. **Set a range** — Both parties agree on a starting amount, ending amount, and interval
2. **Take turns privately** — At each dollar amount, each party indicates Accept or Reject on the same device (hotseat-style), without the other party watching
3. **Reveal only matches** — If both say Accept, the tool announces the settlement amount. If one says Accept and the other says Reject, the Reject party **never learns** the other side accepted

Because a party can say "Yes" without risking their bargaining position, both sides have an incentive to be honest rather than posture.

## Two Ways to Use It

### 🌐 Web Version (Recommended)

Visit **[dvelton.github.io/hotseat-mediator](https://dvelton.github.io/hotseat-mediator/)** in any browser. Works on phones and tablets — perfect for passing a device back and forth. No installation required.

Features:
- Custom party labels (not just Plaintiff/Defendant)
- Input validation and range preview
- Progress indicator
- Privacy-first: all data stays in your browser

### 🐍 Python CLI Version

The original command-line version is still available:

```bash
python hotseat_mediator.py
```

Requires Python 3. Follow the on-screen prompts to set up the range and take turns.

## Background

After practicing law and running a civil litigation practice in Silicon Valley for nearly a decade, I started learning programming for fun. This was the first project — born from watching too many cases stall over negotiation dynamics that a simple algorithm could resolve.

## License

MIT
