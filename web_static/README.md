# AirBnB Clone - Web Static

This project is part of the AirBnB clone series. The goal is to create static web pages using HTML and CSS to build the frontend for the AirBnB platform, without any JavaScript or dynamic data fetching. This series will lay the foundation for building a fully functional web application in future stages.

## Table of Contents
- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [0. Inline Styling](#0-inline-styling)
  - [1. Head Styling](#1-head-styling)
  - [2. CSS Files](#2-css-files)
  - [3. Zoning Done](#3-zoning-done)
  - [4. Search!](#4-search)
  - [5. More Filters](#5-more-filters)
  - [6. It's (H)over](#6-its-hover)
  - [7. Display Results](#7-display-results)
  - [8. More Details](#8-more-details)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The goal of this project is to build the frontend of an AirBnB clone by creating static HTML pages and styling them using CSS. You will be working with different layouts, elements, and applying various styling techniques to meet the design specifications. The pages will be responsive and comply with W3C standards.

### Background Context

The project involves building static HTML pages and styling them without the use of JavaScript or dynamic data. We’ll break down the frontend development into smaller tasks to ensure everything is built step by step.

## Requirements

### General Requirements
- Allowed Editors: `vi`, `vim`, `emacs`
- All files should end with a new line.
- A `README.md` file is required in the root directory.
- Code must be W3C-compliant and pass validation with the [W3C Validator](https://validator.w3.org/).
- All CSS files must be stored in the `styles` folder.
- All images must be stored in the `images` folder.
- No use of `!important` or IDs (`#`).
- You cannot use the `img`, `embed`, or `iframe` tags.
- No JavaScript allowed.
- Screenshots should be based on Chrome version 56 or higher.
- Cross-browser compatibility is not required.

## Tasks

### 0. Inline Styling
- **File**: `0-index.html`
- **Description**: Create an HTML page with a header and footer, styled using inline CSS.
- **Requirements**:
  - Use the `header` and `footer` tags.
  - Apply specific height, width, and color styles directly on the elements using inline styling.
  - No use of external files, style tags, or class IDs.

### 1. Head Styling
- **File**: `1-index.html`
- **Description**: Same as Task 0 but using the `style` tag in the head instead of inline styles.
- **Requirements**:
  - Use `header` and `footer` tags.
  - All styles should be in the `<style>` tag in the `head`.

### 2. CSS Files
- **File**: `2-index.html`, `styles/2-common.css`, `styles/2-header.css`, `styles/2-footer.css`
- **Description**: Use separate CSS files for global styles, header styles, and footer styles.
- **Requirements**:
  - No inline styles or `style` tags in the `head`.
  - Maintain the same layout as in Task 1.

### 3. Zoning Done
- **File**: `3-index.html`, `styles/3-common.css`, `styles/3-header.css`, `styles/3-footer.css`
- **Description**: Refine the layout with additional CSS styles for the body and header.
- **Requirements**:
  - Add a favicon.
  - Header color should be white with specific dimensions and padding.
  - Footer should be centered with specific alignment.
  - No use of the `style` tag or `img` tags.

### 4. Search!
- **File**: `4-index.html`, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/4-filters.css`
- **Description**: Add a search button and filters section to the page layout.
- **Requirements**:
  - Add a `.container` with a filter section and a search button.
  - Filters should be styled with specific dimensions, border, and alignment.

### 5. More Filters
- **File**: `5-index.html`, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/5-filters.css`
- **Description**: Extend the filter section to include location and amenities filters.
- **Requirements**:
  - Use the `h3` and `h4` tags for titles and subtitles.
  - Style filters with specific borders and text.

### 6. It's (H)over
- **File**: `6-index.html`, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/6-filters.css`
- **Description**: Add dropdown functionality for the location and amenities filters.
- **Requirements**:
  - Implement contextual dropdowns for the filters.
  - The `locations` filter should have two levels of options (states and cities).

### 7. Display Results
- **File**: `7-index.html`, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/6-filters.css`, `styles/7-places.css`
- **Description**: Display the results of the search with a "Places" section.
- **Requirements**:
  - Display multiple places with their names and specific styles.
  - Each place should be contained in an `article` tag with specific padding and margin.

### 8. More Details
- **File**: `8-index.html`, `styles/4-common.css`, `styles/3-header.css`, `styles/3-footer.css`, `styles/6-filters.css`, `styles/8-places.css`
- **Description**: Add more details for each place with price, number of rooms, and description.
- **Requirements**:
  - Add price, information, user, and description sections for each place.
  - Price should be displayed in a specific styled box.
  - Owner information should be in bold.

## Installation

To get started with the project, you can clone this repository using the following command:

```bash
git clone https://github.com/your_username/AirBnB_clone.git

