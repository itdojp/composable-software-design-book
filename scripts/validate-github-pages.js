#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const configPath = path.join(root, "_config.yml");
const indexPath = path.join(root, "index.md");
const navPath = path.join(root, "_data", "navigation.json");
const bookConfigPath = path.join(root, "book-config.json");

const expected = {
  title: "Compositional Software Design for Agentic Systems",
  description:
    "A practical guide to designing AI-assisted software systems with composition, diagrams, and effect boundaries that remain auditable and verifiable.",
  author: "ITDO Inc.",
};

function read(pathname) {
  return fs.readFileSync(pathname, "utf8");
}

function expectRegex(text, regex, message, errors) {
  if (!regex.test(text)) {
    errors.push(message);
  }
}

function main() {
  const errors = [];

  if (!fs.existsSync(configPath)) {
    errors.push("missing _config.yml at repository root");
  }
  if (fs.existsSync(path.join(root, "docs", "_config.yml"))) {
    errors.push("unexpected docs/_config.yml found; canonical config should be root _config.yml");
  }
  if (!fs.existsSync(indexPath)) {
    errors.push("missing index.md");
  }
  if (!fs.existsSync(navPath)) {
    errors.push("missing _data/navigation.json");
  }
  if (!fs.existsSync(bookConfigPath)) {
    errors.push("missing book-config.json");
  }

  if (errors.length === 0) {
    const configText = read(configPath);
    const indexText = read(indexPath);
    const nav = JSON.parse(read(navPath));
    const bookConfig = JSON.parse(read(bookConfigPath));

    expectRegex(configText, /^title:\s+"Compositional Software Design for Agentic Systems"$/m, "site title does not match the finalized metadata", errors);
    expectRegex(configText, /^description:\s+"A practical guide to designing AI-assisted software systems with composition, diagrams, and effect boundaries that remain auditable and verifiable\."$/m, "site description does not match the finalized metadata", errors);
    expectRegex(configText, /^author:\s+"ITDO Inc\."$/m, "site author does not match the finalized metadata", errors);
    expectRegex(configText, /^url:\s+"https:\/\/itdojp\.github\.io"$/m, "url is not set to https://itdojp.github.io", errors);
    expectRegex(configText, /^baseurl:\s+"\/composable-software-design-book"$/m, "baseurl is not set to /composable-software-design-book", errors);
    expectRegex(configText, /^repository:\s+"itdojp\/composable-software-design-book"$/m, "repository identity is not set correctly", errors);
    expectRegex(configText, /^defaults:\s*$/m, "defaults block is missing", errors);
    expectRegex(configText, /path:\s*"src"/m, "defaults for src pages are missing", errors);
    expectRegex(configText, /layout:\s*book/m, "layout default for published pages is missing", errors);

    if (/]\((?:\/)?src\/.+\.md\)/.test(indexText)) {
      errors.push("index.md still links to source markdown files instead of published URLs");
    }

    const allNavItems = [
      ...(nav.introduction || []),
      ...(nav.chapters || []),
      ...(nav.appendices || []),
    ];

    if (allNavItems.length === 0) {
      errors.push("navigation.json does not define any navigation items");
    }

    for (const item of allNavItems) {
      if (!item.path || !item.path.startsWith("/")) {
        errors.push(`navigation item path must be absolute from site root: ${JSON.stringify(item)}`);
      }
      if (item.path.endsWith(".md") || item.path.endsWith(".html")) {
        errors.push(`navigation item path should use published page URLs, not source file paths: ${item.path}`);
      }
    }

    if (bookConfig.repository?.url !== "https://github.com/itdojp/composable-software-design-book.git") {
      errors.push("book-config repository URL does not match the GitHub repository");
    }
    if (bookConfig.title !== expected.title || bookConfig.description !== expected.description || bookConfig.author !== expected.author) {
      errors.push("book-config metadata does not match the publishing metadata");
    }
  }

  if (errors.length > 0) {
    console.log("FAIL");
    for (const error of errors) {
      console.log(`- ${error}`);
    }
    process.exit(1);
  }

  console.log("PASS");
}

main();
