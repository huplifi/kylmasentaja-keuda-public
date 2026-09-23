import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Kylmäasentajan muistiinpanot",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "fi-FI",
    baseUrl: "huplifi.github.io/kylmasentaja-keuda-public",
    ignorePatterns: ["Liitteet", "Arkisto", ".*"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "local",
      cdnCaching: false,
      typography: { header: "system-ui", body: "system-ui", code: "ui-monospace" },
      colors: {
        lightMode: {
          light: "#fafbf9", lightgray: "#dde3e4", gray: "#717c83",
          darkgray: "#333f47", dark: "#152a35", secondary: "#205b73", tertiary: "#426e76",
          highlight: "rgba(32, 91, 115, 0.08)", textHighlight: "#d9eacf",
        },
        darkMode: {
          light: "#151c22", lightgray: "#33414b", gray: "#9ba9b2",
          darkgray: "#d2dce2", dark: "#eef3f5", secondary: "#94c9de", tertiary: "#a6c7ba",
          highlight: "rgba(148, 201, 222, 0.10)", textHighlight: "#395545",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.SyntaxHighlighting({ theme: { light: "github-light", dark: "github-dark" }, keepBackground: false }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "absolute" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.ExplicitPublish()],
    emitters: [
      Plugin.ComponentResources(), Plugin.ContentPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: false }),
      Plugin.Static(), Plugin.Favicon(), Plugin.NotFoundPage(),
    ],
  },
}
export default config
