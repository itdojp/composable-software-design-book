#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");

function readYamlValue(text, key) {
  const regex = new RegExp(`^${key}:\\s+"?([^"\\n]+)"?$`, "m");
  const match = text.match(regex);
  return match ? match[1] : null;
}

function main() {
  const configPath = path.join(root, "_config.yml");
  const navPath = path.join(root, "_data", "navigation.json");
  const sitePath = path.join(root, "_site");

  if (!fs.existsSync(configPath) || !fs.existsSync(navPath)) {
    console.log("FAIL");
    console.log("- Missing _config.yml or _data/navigation.json");
    process.exit(1);
  }

  const configText = fs.readFileSync(configPath, "utf8");
  const nav = JSON.parse(fs.readFileSync(navPath, "utf8"));

  const flattenCount = (items) => {
    if (!Array.isArray(items)) {
      return 0;
    }
    if (items.length > 0 && Array.isArray(items[0].items)) {
      return items.reduce((sum, group) => sum + ((group.items || []).length), 0);
    }
    return items.length;
  };

  const summary = {
    configPath: "_config.yml",
    title: readYamlValue(configText, "title"),
    url: readYamlValue(configText, "url"),
    baseurl: readYamlValue(configText, "baseurl"),
    repository: readYamlValue(configText, "repository"),
    frontMatterItems: flattenCount(nav.additional),
    introductionItems: (nav.introduction || []).length,
    chapterItems: flattenCount(nav.chapters),
    appendixItems: (nav.appendices || []).length,
    backmatterItems: flattenCount(nav.backmatter),
    afterwordItems: flattenCount(nav.afterword),
    buildOutputPresent: fs.existsSync(sitePath),
  };

  console.log(JSON.stringify(summary, null, 2));
}

main();
