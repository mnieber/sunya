# Instructions for writing a SelectEffect.tsx file

When writing a SelectEffect.tsx file, please follow the example in blogs/components/SelectBlogEffect.tsx.

## Purpose

The purpose of the SelectEffect is to react to an url-change by selecting a resource using the selection-facet of some resource container.

## UrlEffectView

The UrlEffectView is a small helper component that renders a warning on the screen when the url and the selected resource have diverged (based on the isInSync flag) for more than a brief time interval. This helps to programmer to spot and correct mistakes.
