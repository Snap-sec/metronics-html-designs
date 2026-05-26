---
name: Metronic UI Design Skill
description: Strict guidelines and components for generating new UIs in the Metronic HTML Tailwind theme without using external styling.
---

# Metronic Theme Design Instructions

This document acts as an explicit instruction set (or AI skill) for creating new user interfaces within this application. It guarantees that all new UIs seamlessly integrate into the existing design system without introducing fragmented or unstyled components.

**CRITICAL RULE**: Do not write custom HTML elements styled with external CSS, inline `<style>`, or unstructured Tailwind classes. **You must exclusively use the existing theme's DOM structure and utility classes.** 

## 1. Document & Layout Initialization
For the Metro UI layout and CSS variables to render correctly:
*   **HTML Tag**: Must include `data-kt-theme="true"` and `data-kt-theme-mode="light"` (or check system scripts).
*   **Body Classes**: The `<body>` element **MUST** have the `.demo1` class. Without `.demo1`, container margins, padding, and sidebar variables will fail.
    *   *Example:* `<body class="antialiased flex h-full text-base text-foreground bg-background demo1 kt-header-fixed">`
*   **Theme Script**: You must include the inline initialization script directly inside the body. This script sets the `.light` or `.dark` class on the `<html>` root, which strictly drives the variable colors (like `bg-background`).

## 2. Structural Wrappers
Standard page content uses the flexbox wrapper system:
```html
<div class="flex grow">
  <!-- Content Space -->
  <div class="wrapper flex grow flex-col">
    <!-- Header -->
    <header class="header flex items-center justify-between px-8 bg-background border-b border-b-border h-[70px] shrink-0" id="header">...</header>
    <!-- Main Content -->
    <main class="grow pt-8 pb-8 px-8 flex-1 overflow-auto" id="content">
      <div class="flex flex-col gap-8 w-full max-w-7xl mx-auto">
        <!-- Inside Dashboard Content Here -->
      </div>
    </main>
  </div>
</div>
```

## 3. UI Components (The `kt-` Prefix)

### Containers / Cards
Always wrap grouped content inside a `kt-card`.
*   *Implementation:* `<div class="kt-card p-5 lg:px-7 lg:py-6 rounded-lg border border-border bg-background">`
*   *Headers:* `<h3>` elements should use `text-lg font-semibold text-foreground`.

### Buttons
Control elements utilize the `kt-btn` base class.
*   *Primary:* `<button class="kt-btn kt-btn-primary">Submit</button>`
*   *Outline/Secondary:* `<button class="kt-btn kt-btn-outline">Cancel</button>`
*   *Icon-Only Buttons:* `<button class="kt-btn kt-btn-outline kt-btn-icon size-[30px]"><i class="ki-filled ki-setting-2"></i></button>`

### Forms and Inputs
Inputs feature the `.kt-input` or `.kt-checkbox` classes.
*   *Text Input:* `<input class="kt-input" placeholder="Type..." type="text"/>`
*   *Checkbox:* `<input class="kt-checkbox kt-checkbox-sm" type="checkbox"/>`

### Tables
Do not use raw `<table>` elements. Use the `kt-table` scoping:
```html
<div class="overflow-x-auto">
  <table class="kt-table kt-table-border table-fixed min-w-full text-left bg-background text-sm">
    <thead class="bg-muted/70 text-muted-foreground font-semibold">
      <tr>...</tr>
    </thead>
    <tbody class="divide-y divide-border">
      <tr class="hover:bg-accent/40 transition-colors">
        <td class="p-4">...</td>
      </tr>
    </tbody>
  </table>
</div>
```

## 4. Typography, Badges, and Colors
Metronic employs sophisticated variable-driven Tailwind prefixes.
*   **Colors / Backgrounds**: Use standard prefixes combined with states: `primary`, `success`, `warning`, `danger`, `info`, `muted`, `accent`.
    *   *Examples:* `bg-primary/5`, `text-success`, `border-border`, `text-foreground`, `text-muted-foreground`.
*   **Status Badges / Labels**: Replace plain text priorities/status indicators with colored semi-transparent labels.
    *   *Implementation:* `<span class="inline-flex items-center px-2 py-1 rounded text-xs font-semibold bg-danger/10 text-danger">Critical</span>`

## 5. Icons & Graphical Elements
Do not utilize FontAwesome or SVG injections. The template strictly includes KeenIcons:
*   Use the `<i>` tag with `ki-filled` or `ki-outline`.
*   *Examples:* `ki-filled ki-element-11` (Dashboard), `ki-filled ki-setting-2` (Settings), `ki-outline ki-dots-horizontal` (Menu dots).

---
**Enforcement:**
When tasked with creating a new feature, dashboard, or UI component within this repository, first consult these exact classes snippet examples. Duplicate these HTML semantics exactly rather than attempting to fabricate custom solutions.
