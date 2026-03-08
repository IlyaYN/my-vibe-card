# Project Blueprint

## Overview

A simple, visually appealing personal portfolio or "vcard" website. The site introduces the user, showcases their skills, and provides links to their social/professional profiles. The design is modern, using a dark theme, gradients, and subtle animations.

## Project Structure & Design

### Initial Version:
*   **`index.html`**: The main and only page.
*   **Styling**: Uses Tailwind CSS via CDN for rapid UI development.
*   **Layout**: Centered content on a dark background (`bg-zinc-950`).
*   **Visuals**:
    *   A blurred, rounded background element with an indigo color (`bg-indigo-600`) to create a decorative "glow" effect.
    *   Hero text with a gradient effect for the user's name (`from-indigo-400 to-cyan-400`).
*   **Content**:
    *   Main heading: "Привет, я Илья" (Hello, I'm Ilya).
    *   A short bio paragraph describing the user as a beginner in IT and front-end development.

## Current Plan: Add Social Links

### Goal
To add a section with clickable icons that link to the user's social media profiles (e.g., Telegram, GitHub). This will make the page more interactive and useful.

### Steps
1.  **Add an icon section**: Create a new `div` in `index.html` below the introductory paragraph.
2.  **Add SVG Icons**: Insert SVG code for Telegram and GitHub icons. The icons will be styled with Tailwind CSS to match the site's aesthetic.
3.  **Wrap icons in links**: Each icon will be wrapped in an `<a>` tag with a placeholder `href` (e.g., `#`).
4.  **Apply Styling**:
    *   Use flexbox to arrange the icons horizontally.
    *   Add spacing between the icons.
    *   Apply hover effects to the icons for better interactivity (e.g., change opacity or scale).
