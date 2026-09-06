# Umami Analytics — Red Architecture
## Setup

1. Generate a random salt:
   `openssl rand -base64 32`

2. Replace `HASH_SALT` in docker-compose.yml with that value.

3. Start Umami:
   ```bash
   cd "/home/sky/red studio hermes/analytics"
   docker compose up -d
   ```

4. Visit `http://localhost:3000` and create an admin account.

5. Create a new website with:
   - Name: Red Architecture
   - Domain: your actual domain or `localhost` for testing

6. Copy the tracking script and paste it into `index.html` before `</body>`.

## Integration

Add this before `</body>` in `/home/sky/red studio hermes/index.html`:

```html
<script async defer data-website-id="YOUR_WEBSITE_ID" src="http://localhost:3000/script.js"></script>
```

## Access

- Dashboard: `http://localhost:3000`
- Only accessible from this machine (`127.0.0.1`)
- No external connections, no cookies, no personal data stored

## Privacy

Umami is privacy-first:
- No cookies
- No personal data storage
- IPs are not stored
- Only country-level location, device type, browser, OS, referrer, and page views
