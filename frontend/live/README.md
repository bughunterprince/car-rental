# DriveFlow Frontend - Standalone Preview

This is a **100% pure frontend** - no Django, no backend needed, no dependencies!

## How to Run Locally

1. Open `index.html` in your web browser
2. Navigate through all pages - they're all static HTML with embedded CSS and JavaScript

## Pages Included

- **index.html** - Home page with featured cars
- **cars.html** - Browse full car inventory with filters
- **carsdetail.html** - Individual car details and specs
- **booking.html** - Booking calculation demo
- **login.html** - Login with password or face capture demo
- **register.html** - Registration with face capture demo
- **userdash.html** - User dashboard with booking history
- **admindash.html** - Admin dashboard with Chart.js analytics

## Key Features

✅ No server required
✅ No API calls
✅ No database
✅ Works offline
✅ Face capture functionality (webcam)
✅ Interactive booking calculator
✅ Admin analytics charts
✅ Fully responsive design
✅ Inline CSS for easy styling
✅ Pure JavaScript (Chart.js library from CDN)

## Demo Functionality

- **Login:** Click login, fill demo credentials, get redirected to dashboard
- **Register:** Fill registration form with face capture to see it in action
- **Booking:** Select dates and see total price calculation instantly
- **Face Capture:** Activate webcam, capture image, submit form

## To Deploy

1. Upload entire `frontend/live/` folder to any static hosting (GitHub Pages, Netlify, Vercel, etc.)
2. No build process needed - it's already ready to deploy!
3. For GitHub Pages: Push to `gh-pages` branch

## File Structure

```
frontend/live/
├── index.html          (Home page)
├── cars.html           (Car listing)
├── carsdetail.html     (Car details)
├── booking.html        (Booking form)
├── login.html          (Login page)
├── register.html       (Registration)
├── userdash.html       (User dashboard)
├── admindash.html      (Admin dashboard)
└── assets/
    └── images/         (Car photos)
```

## Notes

- All forms are **demo forms** - they show alerts but don't submit anywhere
- Face capture works with any webcam in supported browsers
- All styling is embedded in HTML files for maximum portability
- External dependencies: Google Fonts (from CDN), Chart.js (from CDN)
