import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(), header: [], afterBody: [],
  footer: Component.Footer({ links: { "Sivuston lähdekoodi": "https://github.com/huplifi/kylmasentaja-keuda-public" } }),
}
const navigation = [
  Component.PageTitle(),
  Component.MobileOnly(Component.Spacer()),
  Component.Flex({ components: [
    { Component: Component.Search(), grow: true },
    { Component: Component.Darkmode() },
  ] }),
  Component.Explorer({
    title: "Opiskele aiheittain", useSavedState: false,
    sortFn: (a, b) => {
      const order = ["index", "kylmatekniikan-perusteet", "kylmaaineet", "sahkoopin-perusteet", "kaavat-ja-yksikot"]
      const aRank = order.includes(a.slugSegment) ? order.indexOf(a.slugSegment) : 99
      const bRank = order.includes(b.slugSegment) ? order.indexOf(b.slugSegment) : 99
      return aRank - bRank || a.displayName.localeCompare(b.displayName, "fi")
    },
  }),
]
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [Component.ArticleTitle()],
  left: navigation,
  right: [Component.TableOfContents()],
}
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.ArticleTitle()], left: navigation, right: [],
}
