# PRELAUNCH.md — Go-Live Checklist

Work through this before anything is public, and again before any major release.
Mark each item `[x]` done, or `N/A` with a reason. Don't skip silently. An agent may run the checks and fill in results, but only the owner signs off.

---

## 1. Secrets & keys
- [ ] No private keys, service-role keys or passwords in frontend code
- [ ] `.env` is in `.gitignore` and not in git history (`git log --all -- .env` returns nothing)
- [ ] Production secrets set in the host's environment settings, not in files
- [ ] Any key that was ever committed has been rotated

## 2. Database & auth (skip if no database)
- [ ] Row-Level Security is ON for every client-exposed table
- [ ] No `USING (true)` policies on private data
- [ ] Tested as a **logged-out visitor** with the public key: private tables return nothing
- [ ] Tested as a **normal user**: can only see and edit their own rows
- [ ] Tested as an **admin**: admin-only actions work, and fail for normal users
- [ ] Password reset, sign-up and email verification flows tested end to end

## 3. Cost & abuse protection
- [ ] Hosting plan's bandwidth limit and overage price written here: ____
- [ ] Hard spending cap or usage limit set on every paid service (hosting, database, APIs, AI)
- [ ] Rate limiting on forms, logins and any API endpoint
- [ ] Bot protection on public forms (e.g. Cloudflare Turnstile)
- [ ] No loops or retries that can run without a limit
- [ ] Kill switch documented: how to take the site/app offline fast: ____

## 4. Accessibility
- [ ] Every page usable with keyboard only (Tab, Shift+Tab, Enter, Esc); focus is visible
- [ ] Every meaningful image has alt text
- [ ] Text contrast at least 4.5:1 (large text 3:1)
- [ ] Every form field has a label; errors are described in text
- [ ] Page has one `<h1>` and headings in order
- [ ] Automated check run (Lighthouse or axe) with no critical issues

## 5. Messaging & privacy (skip if not collecting contact info)
- [ ] SMS/email only sent to people with recorded opt-in consent
- [ ] Every message has a working opt-out (STOP / unsubscribe)
- [ ] Privacy policy page exists and matches what is actually collected

## 6. Function & quality
- [ ] Definition of done from `AGENTS.md` met
- [ ] Tested on mobile and desktop, in at least two browsers
- [ ] Browser console shows no errors on main pages
- [ ] All links work; 404 page exists
- [ ] Contact info, hours and business details are correct (business sites)

## 7. Recovery
- [ ] Code committed and pushed; release tagged
- [ ] Database backup taken (if any) and restore tested at least once
- [ ] Previous version can be redeployed quickly if launch goes wrong

---

**Signed off:** ____ **Date:** ____
