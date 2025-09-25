Title: Getting Started: Project Structure

URL Source: https://nextjs.org/docs/app/getting-started/project-structure

Markdown Content:
Getting Started: Project Structure | Next.js

===============
[Skip to content](https://nextjs.org/docs/app/getting-started/project-structure#geist-skip-nav)

[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_app_getting-started_project-structure "Go to Vercel homepage")

[![Image 35: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true "Go to the homepage")

[](https://nextjs.org/ "Go to the homepage")

Search documentation...CtrlK Search...⌘K

[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_app_getting-started_project-structure "Go to Vercel homepage")

[![Image 36: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true "Go to the homepage")

[](https://nextjs.org/ "Go to the homepage")

[Showcase](https://nextjs.org/showcase)[Docs](https://nextjs.org/docs "Documentation")[Blog](https://nextjs.org/blog)[Templates](https://vercel.com/templates/next.js?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_templates)[Enterprise](https://vercel.com/contact/sales/nextjs?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_enterprise)

Search documentation...CtrlK Search...⌘K Feedback[Learn](https://nextjs.org/learn)

Menu

Using App Router

Features available in /app

Latest Version

15.5.4

*   [Getting Started](https://nextjs.org/docs/app/getting-started)

    *   [Installation](https://nextjs.org/docs/app/getting-started/installation)
    *   [Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
    *   [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)
    *   [Linking and Navigating](https://nextjs.org/docs/app/getting-started/linking-and-navigating)
    *   [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
    *   [Partial Prerendering](https://nextjs.org/docs/app/getting-started/partial-prerendering)
    *   [Fetching Data](https://nextjs.org/docs/app/getting-started/fetching-data)
    *   [Updating Data](https://nextjs.org/docs/app/getting-started/updating-data)
    *   [Caching and Revalidating](https://nextjs.org/docs/app/getting-started/caching-and-revalidating)
    *   [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling)
    *   [CSS](https://nextjs.org/docs/app/getting-started/css)
    *   [Image Optimization](https://nextjs.org/docs/app/getting-started/images)
    *   [Font Optimization](https://nextjs.org/docs/app/getting-started/fonts)
    *   [Metadata and OG images](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)
    *   [Route Handlers and Middleware](https://nextjs.org/docs/app/getting-started/route-handlers-and-middleware)
    *   [Deploying](https://nextjs.org/docs/app/getting-started/deploying)
    *   [Upgrading](https://nextjs.org/docs/app/getting-started/upgrading)

*   [Guides](https://nextjs.org/docs/app/guides)

    *   [Analytics](https://nextjs.org/docs/app/guides/analytics)
    *   [Authentication](https://nextjs.org/docs/app/guides/authentication)
    *   [Backend for Frontend](https://nextjs.org/docs/app/guides/backend-for-frontend)
    *   [Caching](https://nextjs.org/docs/app/guides/caching)
    *   [CI Build Caching](https://nextjs.org/docs/app/guides/ci-build-caching)
    *   [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy)
    *   [CSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)
    *   [Custom Server](https://nextjs.org/docs/app/guides/custom-server)
    *   [Data Security](https://nextjs.org/docs/app/guides/data-security)
    *   [Debugging](https://nextjs.org/docs/app/guides/debugging)
    *   [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode)
    *   [Environment Variables](https://nextjs.org/docs/app/guides/environment-variables)
    *   [Forms](https://nextjs.org/docs/app/guides/forms)
    *   [ISR](https://nextjs.org/docs/app/guides/incremental-static-regeneration)
    *   [Instrumentation](https://nextjs.org/docs/app/guides/instrumentation)
    *   [Internationalization](https://nextjs.org/docs/app/guides/internationalization)
    *   [JSON-LD](https://nextjs.org/docs/app/guides/json-ld)
    *   [Lazy Loading](https://nextjs.org/docs/app/guides/lazy-loading)
    *   [Development Environment](https://nextjs.org/docs/app/guides/local-development)
    *   [MDX](https://nextjs.org/docs/app/guides/mdx)
    *   [Memory Usage](https://nextjs.org/docs/app/guides/memory-usage)
    *   [Migrating](https://nextjs.org/docs/app/guides/migrating)

        *   [App Router](https://nextjs.org/docs/app/guides/migrating/app-router-migration)
        *   [Create React App](https://nextjs.org/docs/app/guides/migrating/from-create-react-app)
        *   [Vite](https://nextjs.org/docs/app/guides/migrating/from-vite)

    *   [Multi-tenant](https://nextjs.org/docs/app/guides/multi-tenant)
    *   [Multi-zones](https://nextjs.org/docs/app/guides/multi-zones)
    *   [OpenTelemetry](https://nextjs.org/docs/app/guides/open-telemetry)
    *   [Package Bundling](https://nextjs.org/docs/app/guides/package-bundling)
    *   [Prefetching](https://nextjs.org/docs/app/guides/prefetching)
    *   [Production](https://nextjs.org/docs/app/guides/production-checklist)
    *   [PWAs](https://nextjs.org/docs/app/guides/progressive-web-apps)
    *   [Redirecting](https://nextjs.org/docs/app/guides/redirecting)
    *   [Sass](https://nextjs.org/docs/app/guides/sass)
    *   [Scripts](https://nextjs.org/docs/app/guides/scripts)
    *   [Self-Hosting](https://nextjs.org/docs/app/guides/self-hosting)
    *   [SPAs](https://nextjs.org/docs/app/guides/single-page-applications)
    *   [Static Exports](https://nextjs.org/docs/app/guides/static-exports)
    *   [Tailwind CSS v3](https://nextjs.org/docs/app/guides/tailwind-v3-css)
    *   [Testing](https://nextjs.org/docs/app/guides/testing)

        *   [Cypress](https://nextjs.org/docs/app/guides/testing/cypress)
        *   [Jest](https://nextjs.org/docs/app/guides/testing/jest)
        *   [Playwright](https://nextjs.org/docs/app/guides/testing/playwright)
        *   [Vitest](https://nextjs.org/docs/app/guides/testing/vitest)

    *   [Third Party Libraries](https://nextjs.org/docs/app/guides/third-party-libraries)
    *   [Upgrading](https://nextjs.org/docs/app/guides/upgrading)

        *   [Codemods](https://nextjs.org/docs/app/guides/upgrading/codemods)
        *   [Version 14](https://nextjs.org/docs/app/guides/upgrading/version-14)
        *   [Version 15](https://nextjs.org/docs/app/guides/upgrading/version-15)

    *   [Videos](https://nextjs.org/docs/app/guides/videos)

*   [API Reference](https://nextjs.org/docs/app/api-reference)

    *   [Directives](https://nextjs.org/docs/app/api-reference/directives)

        *   [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)
        *   [use client](https://nextjs.org/docs/app/api-reference/directives/use-client)
        *   [use server](https://nextjs.org/docs/app/api-reference/directives/use-server)

    *   [Components](https://nextjs.org/docs/app/api-reference/components)

        *   [Font](https://nextjs.org/docs/app/api-reference/components/font)
        *   [Form Component](https://nextjs.org/docs/app/api-reference/components/form)
        *   [Image Component](https://nextjs.org/docs/app/api-reference/components/image)
        *   [Link Component](https://nextjs.org/docs/app/api-reference/components/link)
        *   [Script Component](https://nextjs.org/docs/app/api-reference/components/script)

    *   [File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)

        *   [default.js](https://nextjs.org/docs/app/api-reference/file-conventions/default)
        *   [Dynamic Segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)
        *   [error.js](https://nextjs.org/docs/app/api-reference/file-conventions/error)
        *   [forbidden.js](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
        *   [instrumentation.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)
        *   [instrumentation-client.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client)
        *   [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes)
        *   [layout.js](https://nextjs.org/docs/app/api-reference/file-conventions/layout)
        *   [loading.js](https://nextjs.org/docs/app/api-reference/file-conventions/loading)
        *   [mdx-components.js](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components)
        *   [middleware.js](https://nextjs.org/docs/app/api-reference/file-conventions/middleware)
        *   [not-found.js](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)
        *   [page.js](https://nextjs.org/docs/app/api-reference/file-conventions/page)
        *   [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes)
        *   [public](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)
        *   [route.js](https://nextjs.org/docs/app/api-reference/file-conventions/route)
        *   [Route Groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups)
        *   [Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)
        *   [src](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)
        *   [template.js](https://nextjs.org/docs/app/api-reference/file-conventions/template)
        *   [unauthorized.js](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
        *   [Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)

            *   [favicon, icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
            *   [manifest.json](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
            *   [opengraph-image and twitter-image](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
            *   [robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)
            *   [sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)

    *   [Functions](https://nextjs.org/docs/app/api-reference/functions)

        *   [after](https://nextjs.org/docs/app/api-reference/functions/after)
        *   [cacheLife](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
        *   [cacheTag](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
        *   [connection](https://nextjs.org/docs/app/api-reference/functions/connection)
        *   [cookies](https://nextjs.org/docs/app/api-reference/functions/cookies)
        *   [draftMode](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
        *   [fetch](https://nextjs.org/docs/app/api-reference/functions/fetch)
        *   [forbidden](https://nextjs.org/docs/app/api-reference/functions/forbidden)
        *   [generateImageMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)
        *   [generateMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)
        *   [generateSitemaps](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps)
        *   [generateStaticParams](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)
        *   [generateViewport](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)
        *   [headers](https://nextjs.org/docs/app/api-reference/functions/headers)
        *   [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response)
        *   [NextRequest](https://nextjs.org/docs/app/api-reference/functions/next-request)
        *   [NextResponse](https://nextjs.org/docs/app/api-reference/functions/next-response)
        *   [notFound](https://nextjs.org/docs/app/api-reference/functions/not-found)
        *   [permanentRedirect](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)
        *   [redirect](https://nextjs.org/docs/app/api-reference/functions/redirect)
        *   [revalidatePath](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)
        *   [revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
        *   [unauthorized](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
        *   [unstable_cache](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)
        *   [unstable_noStore](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore)
        *   [unstable_rethrow](https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow)
        *   [useLinkStatus](https://nextjs.org/docs/app/api-reference/functions/use-link-status)
        *   [useParams](https://nextjs.org/docs/app/api-reference/functions/use-params)
        *   [usePathname](https://nextjs.org/docs/app/api-reference/functions/use-pathname)
        *   [useReportWebVitals](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals)
        *   [useRouter](https://nextjs.org/docs/app/api-reference/functions/use-router)
        *   [useSearchParams](https://nextjs.org/docs/app/api-reference/functions/use-search-params)
        *   [useSelectedLayoutSegment](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment)
        *   [useSelectedLayoutSegments](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)
        *   [userAgent](https://nextjs.org/docs/app/api-reference/functions/userAgent)

    *   [Configuration](https://nextjs.org/docs/app/api-reference/config)

        *   [next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)

            *   [allowedDevOrigins](https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins)
            *   [appDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir)
            *   [assetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)
            *   [authInterrupts](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)
            *   [basePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)
            *   [browserDebugInfoInTerminal](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal)
            *   [cacheComponents](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
            *   [cacheLife](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)
            *   [compress](https://nextjs.org/docs/app/api-reference/config/next-config-js/compress)
            *   [crossOrigin](https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin)
            *   [cssChunking](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking)
            *   [devIndicators](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators)
            *   [distDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir)
            *   [env](https://nextjs.org/docs/app/api-reference/config/next-config-js/env)
            *   [eslint](https://nextjs.org/docs/app/api-reference/config/next-config-js/eslint)
            *   [expireTime](https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime)
            *   [exportPathMap](https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap)
            *   [generateBuildId](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId)
            *   [generateEtags](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags)
            *   [headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)
            *   [htmlLimitedBots](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots)
            *   [httpAgentOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions)
            *   [images](https://nextjs.org/docs/app/api-reference/config/next-config-js/images)
            *   [cacheHandler](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)
            *   [inlineCss](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss)
            *   [logging](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging)
            *   [mdxRs](https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs)
            *   [onDemandEntries](https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries)
            *   [optimizePackageImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)
            *   [output](https://nextjs.org/docs/app/api-reference/config/next-config-js/output)
            *   [pageExtensions](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)
            *   [poweredByHeader](https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader)
            *   [ppr](https://nextjs.org/docs/app/api-reference/config/next-config-js/ppr)
            *   [productionBrowserSourceMaps](https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [reactCompiler](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler)
            *   [reactMaxHeadersLength](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)
            *   [reactStrictMode](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode)
            *   [redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
            *   [rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)
            *   [sassOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions)
            *   [serverActions](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)
            *   [serverComponentsHmrCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)
            *   [serverExternalPackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages)
            *   [staleTimes](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)
            *   [staticGeneration*](https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration)
            *   [taint](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint)
            *   [trailingSlash](https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash)
            *   [transpilePackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages)
            *   [turbopack](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)
            *   [turbopackPersistentCaching](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackPersistentCaching)
            *   [typedRoutes](https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes)
            *   [typescript](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript)
            *   [urlImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports)
            *   [useCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/useCache)
            *   [useLightningcss](https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss)
            *   [viewTransition](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition)
            *   [webpack](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack)
            *   [webVitalsAttribution](https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution)

        *   [TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript)
        *   [ESLint](https://nextjs.org/docs/app/api-reference/config/eslint)

    *   [CLI](https://nextjs.org/docs/app/api-reference/cli)

        *   [create-next-app](https://nextjs.org/docs/app/api-reference/cli/create-next-app)
        *   [next CLI](https://nextjs.org/docs/app/api-reference/cli/next)

    *   [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)
    *   [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)

*   [Getting Started](https://nextjs.org/docs/pages/getting-started)

    *   [Installation](https://nextjs.org/docs/pages/getting-started/installation)
    *   [Project Structure](https://nextjs.org/docs/pages/getting-started/project-structure)
    *   [Images](https://nextjs.org/docs/pages/getting-started/images)
    *   [Fonts](https://nextjs.org/docs/pages/getting-started/fonts)
    *   [CSS](https://nextjs.org/docs/pages/getting-started/css)
    *   [Deploying](https://nextjs.org/docs/pages/getting-started/deploying)

*   [Guides](https://nextjs.org/docs/pages/guides)

    *   [AMP](https://nextjs.org/docs/pages/guides/amp)
    *   [Analytics](https://nextjs.org/docs/pages/guides/analytics)
    *   [Authentication](https://nextjs.org/docs/pages/guides/authentication)
    *   [Babel](https://nextjs.org/docs/pages/guides/babel)
    *   [CI Build Caching](https://nextjs.org/docs/pages/guides/ci-build-caching)
    *   [Content Security Policy](https://nextjs.org/docs/pages/guides/content-security-policy)
    *   [CSS-in-JS](https://nextjs.org/docs/pages/guides/css-in-js)
    *   [Custom Server](https://nextjs.org/docs/pages/guides/custom-server)
    *   [Debugging](https://nextjs.org/docs/pages/guides/debugging)
    *   [Draft Mode](https://nextjs.org/docs/pages/guides/draft-mode)
    *   [Environment Variables](https://nextjs.org/docs/pages/guides/environment-variables)
    *   [Forms](https://nextjs.org/docs/pages/guides/forms)
    *   [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)
    *   [Instrumentation](https://nextjs.org/docs/pages/guides/instrumentation)
    *   [Internationalization](https://nextjs.org/docs/pages/guides/internationalization)
    *   [Lazy Loading](https://nextjs.org/docs/pages/guides/lazy-loading)
    *   [MDX](https://nextjs.org/docs/pages/guides/mdx)
    *   [Migrating](https://nextjs.org/docs/pages/guides/migrating)

        *   [App Router](https://nextjs.org/docs/pages/guides/migrating/app-router-migration)
        *   [Create React App](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app)
        *   [Vite](https://nextjs.org/docs/pages/guides/migrating/from-vite)

    *   [Multi-Zones](https://nextjs.org/docs/pages/guides/multi-zones)
    *   [OpenTelemetry](https://nextjs.org/docs/pages/guides/open-telemetry)
    *   [Package Bundling](https://nextjs.org/docs/pages/guides/package-bundling)
    *   [PostCSS](https://nextjs.org/docs/pages/guides/post-css)
    *   [Preview Mode](https://nextjs.org/docs/pages/guides/preview-mode)
    *   [Production](https://nextjs.org/docs/pages/guides/production-checklist)
    *   [Redirecting](https://nextjs.org/docs/pages/guides/redirecting)
    *   [Sass](https://nextjs.org/docs/pages/guides/sass)
    *   [Scripts](https://nextjs.org/docs/pages/guides/scripts)
    *   [Self-Hosting](https://nextjs.org/docs/pages/guides/self-hosting)
    *   [Static Exports](https://nextjs.org/docs/pages/guides/static-exports)
    *   [Tailwind CSS](https://nextjs.org/docs/pages/guides/tailwind-v3-css)
    *   [Testing](https://nextjs.org/docs/pages/guides/testing)

        *   [Cypress](https://nextjs.org/docs/pages/guides/testing/cypress)
        *   [Jest](https://nextjs.org/docs/pages/guides/testing/jest)
        *   [Playwright](https://nextjs.org/docs/pages/guides/testing/playwright)
        *   [Vitest](https://nextjs.org/docs/pages/guides/testing/vitest)

    *   [Third Party Libraries](https://nextjs.org/docs/pages/guides/third-party-libraries)
    *   [Upgrading](https://nextjs.org/docs/pages/guides/upgrading)

        *   [Codemods](https://nextjs.org/docs/pages/guides/upgrading/codemods)
        *   [Version 10](https://nextjs.org/docs/pages/guides/upgrading/version-10)
        *   [Version 11](https://nextjs.org/docs/pages/guides/upgrading/version-11)
        *   [Version 12](https://nextjs.org/docs/pages/guides/upgrading/version-12)
        *   [Version 13](https://nextjs.org/docs/pages/guides/upgrading/version-13)
        *   [Version 14](https://nextjs.org/docs/pages/guides/upgrading/version-14)
        *   [Version 9](https://nextjs.org/docs/pages/guides/upgrading/version-9)

*   [Building Your Application](https://nextjs.org/docs/pages/building-your-application)

    *   [Routing](https://nextjs.org/docs/pages/building-your-application/routing)

        *   [Pages and Layouts](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)
        *   [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)
        *   [Linking and Navigating](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating)
        *   [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)
        *   [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)
        *   [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
        *   [Custom Errors](https://nextjs.org/docs/pages/building-your-application/routing/custom-error)

    *   [Rendering](https://nextjs.org/docs/pages/building-your-application/rendering)

        *   [Server-side Rendering (SSR)](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)
        *   [Static Site Generation (SSG)](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)
        *   [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)
        *   [Client-side Rendering (CSR)](https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering)

    *   [Data Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching)

        *   [getStaticProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
        *   [getStaticPaths](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)
        *   [Forms and Mutations](https://nextjs.org/docs/pages/building-your-application/data-fetching/forms-and-mutations)
        *   [getServerSideProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
        *   [Client-side Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)

    *   [Configuring](https://nextjs.org/docs/pages/building-your-application/configuring)

        *   [Error Handling](https://nextjs.org/docs/pages/building-your-application/configuring/error-handling)

*   [API Reference](https://nextjs.org/docs/pages/api-reference)

    *   [Components](https://nextjs.org/docs/pages/api-reference/components)

        *   [Font](https://nextjs.org/docs/pages/api-reference/components/font)
        *   [Form](https://nextjs.org/docs/pages/api-reference/components/form)
        *   [Head](https://nextjs.org/docs/pages/api-reference/components/head)
        *   [Image](https://nextjs.org/docs/pages/api-reference/components/image)
        *   [Image (Legacy)](https://nextjs.org/docs/pages/api-reference/components/image-legacy)
        *   [Link](https://nextjs.org/docs/pages/api-reference/components/link)
        *   [Script](https://nextjs.org/docs/pages/api-reference/components/script)

    *   [File-system conventions](https://nextjs.org/docs/pages/api-reference/file-conventions)

        *   [instrumentation.js](https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation)
        *   [Middleware](https://nextjs.org/docs/pages/api-reference/file-conventions/middleware)
        *   [public](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder)
        *   [src Directory](https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder)

    *   [Functions](https://nextjs.org/docs/pages/api-reference/functions)

        *   [getInitialProps](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props)
        *   [getServerSideProps](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props)
        *   [getStaticPaths](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths)
        *   [getStaticProps](https://nextjs.org/docs/pages/api-reference/functions/get-static-props)
        *   [NextRequest](https://nextjs.org/docs/pages/api-reference/functions/next-request)
        *   [NextResponse](https://nextjs.org/docs/pages/api-reference/functions/next-response)
        *   [useAmp](https://nextjs.org/docs/pages/api-reference/functions/use-amp)
        *   [useReportWebVitals](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals)
        *   [useRouter](https://nextjs.org/docs/pages/api-reference/functions/use-router)
        *   [userAgent](https://nextjs.org/docs/pages/api-reference/functions/userAgent)

    *   [Configuration](https://nextjs.org/docs/pages/api-reference/config)

        *   [next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)

            *   [allowedDevOrigins](https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins)
            *   [assetPrefix](https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix)
            *   [basePath](https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath)
            *   [bundlePagesRouterDependencies](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)
            *   [compress](https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress)
            *   [crossOrigin](https://nextjs.org/docs/pages/api-reference/config/next-config-js/crossOrigin)
            *   [devIndicators](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators)
            *   [distDir](https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir)
            *   [env](https://nextjs.org/docs/pages/api-reference/config/next-config-js/env)
            *   [eslint](https://nextjs.org/docs/pages/api-reference/config/next-config-js/eslint)
            *   [exportPathMap](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap)
            *   [generateBuildId](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId)
            *   [generateEtags](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags)
            *   [headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)
            *   [httpAgentOptions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions)
            *   [images](https://nextjs.org/docs/pages/api-reference/config/next-config-js/images)
            *   [onDemandEntries](https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries)
            *   [optimizePackageImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports)
            *   [output](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output)
            *   [pageExtensions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions)
            *   [poweredByHeader](https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader)
            *   [productionBrowserSourceMaps](https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [reactStrictMode](https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode)
            *   [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)
            *   [rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites)
            *   [Runtime Config](https://nextjs.org/docs/pages/api-reference/config/next-config-js/runtime-configuration)
            *   [serverExternalPackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages)
            *   [trailingSlash](https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash)
            *   [transpilePackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages)
            *   [turbo](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbo)
            *   [typescript](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript)
            *   [urlImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports)
            *   [useLightningcss](https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss)
            *   [webpack](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack)
            *   [webVitalsAttribution](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)

        *   [TypeScript](https://nextjs.org/docs/pages/api-reference/config/typescript)
        *   [ESLint](https://nextjs.org/docs/pages/api-reference/config/eslint)

    *   [CLI](https://nextjs.org/docs/pages/api-reference/cli)

        *   [create-next-app CLI](https://nextjs.org/docs/pages/api-reference/cli/create-next-app)
        *   [next CLI](https://nextjs.org/docs/pages/api-reference/cli/next)

    *   [Edge Runtime](https://nextjs.org/docs/pages/api-reference/edge)
    *   [Turbopack](https://nextjs.org/docs/pages/api-reference/turbopack)

*   [Architecture](https://nextjs.org/docs/architecture)

    *   [Accessibility](https://nextjs.org/docs/architecture/accessibility)
    *   [Fast Refresh](https://nextjs.org/docs/architecture/fast-refresh)
    *   [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler)
    *   [Supported Browsers](https://nextjs.org/docs/architecture/supported-browsers)

*   [Community](https://nextjs.org/docs/community)

    *   [Contribution Guide](https://nextjs.org/docs/community/contribution-guide)
    *   [Rspack](https://nextjs.org/docs/community/rspack)

Using App Router

Features available in /app

Latest Version

15.5.4

*   [Getting Started](https://nextjs.org/docs/app/getting-started)

    *   [Installation](https://nextjs.org/docs/app/getting-started/installation)
    *   [Project Structure](https://nextjs.org/docs/app/getting-started/project-structure)
    *   [Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)
    *   [Linking and Navigating](https://nextjs.org/docs/app/getting-started/linking-and-navigating)
    *   [Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
    *   [Partial Prerendering](https://nextjs.org/docs/app/getting-started/partial-prerendering)
    *   [Fetching Data](https://nextjs.org/docs/app/getting-started/fetching-data)
    *   [Updating Data](https://nextjs.org/docs/app/getting-started/updating-data)
    *   [Caching and Revalidating](https://nextjs.org/docs/app/getting-started/caching-and-revalidating)
    *   [Error Handling](https://nextjs.org/docs/app/getting-started/error-handling)
    *   [CSS](https://nextjs.org/docs/app/getting-started/css)
    *   [Image Optimization](https://nextjs.org/docs/app/getting-started/images)
    *   [Font Optimization](https://nextjs.org/docs/app/getting-started/fonts)
    *   [Metadata and OG images](https://nextjs.org/docs/app/getting-started/metadata-and-og-images)
    *   [Route Handlers and Middleware](https://nextjs.org/docs/app/getting-started/route-handlers-and-middleware)
    *   [Deploying](https://nextjs.org/docs/app/getting-started/deploying)
    *   [Upgrading](https://nextjs.org/docs/app/getting-started/upgrading)

*   [Guides](https://nextjs.org/docs/app/guides)

    *   [Analytics](https://nextjs.org/docs/app/guides/analytics)
    *   [Authentication](https://nextjs.org/docs/app/guides/authentication)
    *   [Backend for Frontend](https://nextjs.org/docs/app/guides/backend-for-frontend)
    *   [Caching](https://nextjs.org/docs/app/guides/caching)
    *   [CI Build Caching](https://nextjs.org/docs/app/guides/ci-build-caching)
    *   [Content Security Policy](https://nextjs.org/docs/app/guides/content-security-policy)
    *   [CSS-in-JS](https://nextjs.org/docs/app/guides/css-in-js)
    *   [Custom Server](https://nextjs.org/docs/app/guides/custom-server)
    *   [Data Security](https://nextjs.org/docs/app/guides/data-security)
    *   [Debugging](https://nextjs.org/docs/app/guides/debugging)
    *   [Draft Mode](https://nextjs.org/docs/app/guides/draft-mode)
    *   [Environment Variables](https://nextjs.org/docs/app/guides/environment-variables)
    *   [Forms](https://nextjs.org/docs/app/guides/forms)
    *   [ISR](https://nextjs.org/docs/app/guides/incremental-static-regeneration)
    *   [Instrumentation](https://nextjs.org/docs/app/guides/instrumentation)
    *   [Internationalization](https://nextjs.org/docs/app/guides/internationalization)
    *   [JSON-LD](https://nextjs.org/docs/app/guides/json-ld)
    *   [Lazy Loading](https://nextjs.org/docs/app/guides/lazy-loading)
    *   [Development Environment](https://nextjs.org/docs/app/guides/local-development)
    *   [MDX](https://nextjs.org/docs/app/guides/mdx)
    *   [Memory Usage](https://nextjs.org/docs/app/guides/memory-usage)
    *   [Migrating](https://nextjs.org/docs/app/guides/migrating)

        *   [App Router](https://nextjs.org/docs/app/guides/migrating/app-router-migration)
        *   [Create React App](https://nextjs.org/docs/app/guides/migrating/from-create-react-app)
        *   [Vite](https://nextjs.org/docs/app/guides/migrating/from-vite)

    *   [Multi-tenant](https://nextjs.org/docs/app/guides/multi-tenant)
    *   [Multi-zones](https://nextjs.org/docs/app/guides/multi-zones)
    *   [OpenTelemetry](https://nextjs.org/docs/app/guides/open-telemetry)
    *   [Package Bundling](https://nextjs.org/docs/app/guides/package-bundling)
    *   [Prefetching](https://nextjs.org/docs/app/guides/prefetching)
    *   [Production](https://nextjs.org/docs/app/guides/production-checklist)
    *   [PWAs](https://nextjs.org/docs/app/guides/progressive-web-apps)
    *   [Redirecting](https://nextjs.org/docs/app/guides/redirecting)
    *   [Sass](https://nextjs.org/docs/app/guides/sass)
    *   [Scripts](https://nextjs.org/docs/app/guides/scripts)
    *   [Self-Hosting](https://nextjs.org/docs/app/guides/self-hosting)
    *   [SPAs](https://nextjs.org/docs/app/guides/single-page-applications)
    *   [Static Exports](https://nextjs.org/docs/app/guides/static-exports)
    *   [Tailwind CSS v3](https://nextjs.org/docs/app/guides/tailwind-v3-css)
    *   [Testing](https://nextjs.org/docs/app/guides/testing)

        *   [Cypress](https://nextjs.org/docs/app/guides/testing/cypress)
        *   [Jest](https://nextjs.org/docs/app/guides/testing/jest)
        *   [Playwright](https://nextjs.org/docs/app/guides/testing/playwright)
        *   [Vitest](https://nextjs.org/docs/app/guides/testing/vitest)

    *   [Third Party Libraries](https://nextjs.org/docs/app/guides/third-party-libraries)
    *   [Upgrading](https://nextjs.org/docs/app/guides/upgrading)

        *   [Codemods](https://nextjs.org/docs/app/guides/upgrading/codemods)
        *   [Version 14](https://nextjs.org/docs/app/guides/upgrading/version-14)
        *   [Version 15](https://nextjs.org/docs/app/guides/upgrading/version-15)

    *   [Videos](https://nextjs.org/docs/app/guides/videos)

*   [API Reference](https://nextjs.org/docs/app/api-reference)

    *   [Directives](https://nextjs.org/docs/app/api-reference/directives)

        *   [use cache](https://nextjs.org/docs/app/api-reference/directives/use-cache)
        *   [use client](https://nextjs.org/docs/app/api-reference/directives/use-client)
        *   [use server](https://nextjs.org/docs/app/api-reference/directives/use-server)

    *   [Components](https://nextjs.org/docs/app/api-reference/components)

        *   [Font](https://nextjs.org/docs/app/api-reference/components/font)
        *   [Form Component](https://nextjs.org/docs/app/api-reference/components/form)
        *   [Image Component](https://nextjs.org/docs/app/api-reference/components/image)
        *   [Link Component](https://nextjs.org/docs/app/api-reference/components/link)
        *   [Script Component](https://nextjs.org/docs/app/api-reference/components/script)

    *   [File-system conventions](https://nextjs.org/docs/app/api-reference/file-conventions)

        *   [default.js](https://nextjs.org/docs/app/api-reference/file-conventions/default)
        *   [Dynamic Segments](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes)
        *   [error.js](https://nextjs.org/docs/app/api-reference/file-conventions/error)
        *   [forbidden.js](https://nextjs.org/docs/app/api-reference/file-conventions/forbidden)
        *   [instrumentation.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation)
        *   [instrumentation-client.js](https://nextjs.org/docs/app/api-reference/file-conventions/instrumentation-client)
        *   [Intercepting Routes](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes)
        *   [layout.js](https://nextjs.org/docs/app/api-reference/file-conventions/layout)
        *   [loading.js](https://nextjs.org/docs/app/api-reference/file-conventions/loading)
        *   [mdx-components.js](https://nextjs.org/docs/app/api-reference/file-conventions/mdx-components)
        *   [middleware.js](https://nextjs.org/docs/app/api-reference/file-conventions/middleware)
        *   [not-found.js](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)
        *   [page.js](https://nextjs.org/docs/app/api-reference/file-conventions/page)
        *   [Parallel Routes](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes)
        *   [public](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder)
        *   [route.js](https://nextjs.org/docs/app/api-reference/file-conventions/route)
        *   [Route Groups](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups)
        *   [Route Segment Config](https://nextjs.org/docs/app/api-reference/file-conventions/route-segment-config)
        *   [src](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder)
        *   [template.js](https://nextjs.org/docs/app/api-reference/file-conventions/template)
        *   [unauthorized.js](https://nextjs.org/docs/app/api-reference/file-conventions/unauthorized)
        *   [Metadata Files](https://nextjs.org/docs/app/api-reference/file-conventions/metadata)

            *   [favicon, icon, and apple-icon](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons)
            *   [manifest.json](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/manifest)
            *   [opengraph-image and twitter-image](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image)
            *   [robots.txt](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots)
            *   [sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)

    *   [Functions](https://nextjs.org/docs/app/api-reference/functions)

        *   [after](https://nextjs.org/docs/app/api-reference/functions/after)
        *   [cacheLife](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
        *   [cacheTag](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
        *   [connection](https://nextjs.org/docs/app/api-reference/functions/connection)
        *   [cookies](https://nextjs.org/docs/app/api-reference/functions/cookies)
        *   [draftMode](https://nextjs.org/docs/app/api-reference/functions/draft-mode)
        *   [fetch](https://nextjs.org/docs/app/api-reference/functions/fetch)
        *   [forbidden](https://nextjs.org/docs/app/api-reference/functions/forbidden)
        *   [generateImageMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-image-metadata)
        *   [generateMetadata](https://nextjs.org/docs/app/api-reference/functions/generate-metadata)
        *   [generateSitemaps](https://nextjs.org/docs/app/api-reference/functions/generate-sitemaps)
        *   [generateStaticParams](https://nextjs.org/docs/app/api-reference/functions/generate-static-params)
        *   [generateViewport](https://nextjs.org/docs/app/api-reference/functions/generate-viewport)
        *   [headers](https://nextjs.org/docs/app/api-reference/functions/headers)
        *   [ImageResponse](https://nextjs.org/docs/app/api-reference/functions/image-response)
        *   [NextRequest](https://nextjs.org/docs/app/api-reference/functions/next-request)
        *   [NextResponse](https://nextjs.org/docs/app/api-reference/functions/next-response)
        *   [notFound](https://nextjs.org/docs/app/api-reference/functions/not-found)
        *   [permanentRedirect](https://nextjs.org/docs/app/api-reference/functions/permanentRedirect)
        *   [redirect](https://nextjs.org/docs/app/api-reference/functions/redirect)
        *   [revalidatePath](https://nextjs.org/docs/app/api-reference/functions/revalidatePath)
        *   [revalidateTag](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
        *   [unauthorized](https://nextjs.org/docs/app/api-reference/functions/unauthorized)
        *   [unstable_cache](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)
        *   [unstable_noStore](https://nextjs.org/docs/app/api-reference/functions/unstable_noStore)
        *   [unstable_rethrow](https://nextjs.org/docs/app/api-reference/functions/unstable_rethrow)
        *   [useLinkStatus](https://nextjs.org/docs/app/api-reference/functions/use-link-status)
        *   [useParams](https://nextjs.org/docs/app/api-reference/functions/use-params)
        *   [usePathname](https://nextjs.org/docs/app/api-reference/functions/use-pathname)
        *   [useReportWebVitals](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals)
        *   [useRouter](https://nextjs.org/docs/app/api-reference/functions/use-router)
        *   [useSearchParams](https://nextjs.org/docs/app/api-reference/functions/use-search-params)
        *   [useSelectedLayoutSegment](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segment)
        *   [useSelectedLayoutSegments](https://nextjs.org/docs/app/api-reference/functions/use-selected-layout-segments)
        *   [userAgent](https://nextjs.org/docs/app/api-reference/functions/userAgent)

    *   [Configuration](https://nextjs.org/docs/app/api-reference/config)

        *   [next.config.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)

            *   [allowedDevOrigins](https://nextjs.org/docs/app/api-reference/config/next-config-js/allowedDevOrigins)
            *   [appDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/appDir)
            *   [assetPrefix](https://nextjs.org/docs/app/api-reference/config/next-config-js/assetPrefix)
            *   [authInterrupts](https://nextjs.org/docs/app/api-reference/config/next-config-js/authInterrupts)
            *   [basePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)
            *   [browserDebugInfoInTerminal](https://nextjs.org/docs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal)
            *   [cacheComponents](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
            *   [cacheLife](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheLife)
            *   [compress](https://nextjs.org/docs/app/api-reference/config/next-config-js/compress)
            *   [crossOrigin](https://nextjs.org/docs/app/api-reference/config/next-config-js/crossOrigin)
            *   [cssChunking](https://nextjs.org/docs/app/api-reference/config/next-config-js/cssChunking)
            *   [devIndicators](https://nextjs.org/docs/app/api-reference/config/next-config-js/devIndicators)
            *   [distDir](https://nextjs.org/docs/app/api-reference/config/next-config-js/distDir)
            *   [env](https://nextjs.org/docs/app/api-reference/config/next-config-js/env)
            *   [eslint](https://nextjs.org/docs/app/api-reference/config/next-config-js/eslint)
            *   [expireTime](https://nextjs.org/docs/app/api-reference/config/next-config-js/expireTime)
            *   [exportPathMap](https://nextjs.org/docs/app/api-reference/config/next-config-js/exportPathMap)
            *   [generateBuildId](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateBuildId)
            *   [generateEtags](https://nextjs.org/docs/app/api-reference/config/next-config-js/generateEtags)
            *   [headers](https://nextjs.org/docs/app/api-reference/config/next-config-js/headers)
            *   [htmlLimitedBots](https://nextjs.org/docs/app/api-reference/config/next-config-js/htmlLimitedBots)
            *   [httpAgentOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/httpAgentOptions)
            *   [images](https://nextjs.org/docs/app/api-reference/config/next-config-js/images)
            *   [cacheHandler](https://nextjs.org/docs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath)
            *   [inlineCss](https://nextjs.org/docs/app/api-reference/config/next-config-js/inlineCss)
            *   [logging](https://nextjs.org/docs/app/api-reference/config/next-config-js/logging)
            *   [mdxRs](https://nextjs.org/docs/app/api-reference/config/next-config-js/mdxRs)
            *   [onDemandEntries](https://nextjs.org/docs/app/api-reference/config/next-config-js/onDemandEntries)
            *   [optimizePackageImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)
            *   [output](https://nextjs.org/docs/app/api-reference/config/next-config-js/output)
            *   [pageExtensions](https://nextjs.org/docs/app/api-reference/config/next-config-js/pageExtensions)
            *   [poweredByHeader](https://nextjs.org/docs/app/api-reference/config/next-config-js/poweredByHeader)
            *   [ppr](https://nextjs.org/docs/app/api-reference/config/next-config-js/ppr)
            *   [productionBrowserSourceMaps](https://nextjs.org/docs/app/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [reactCompiler](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactCompiler)
            *   [reactMaxHeadersLength](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactMaxHeadersLength)
            *   [reactStrictMode](https://nextjs.org/docs/app/api-reference/config/next-config-js/reactStrictMode)
            *   [redirects](https://nextjs.org/docs/app/api-reference/config/next-config-js/redirects)
            *   [rewrites](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)
            *   [sassOptions](https://nextjs.org/docs/app/api-reference/config/next-config-js/sassOptions)
            *   [serverActions](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions)
            *   [serverComponentsHmrCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverComponentsHmrCache)
            *   [serverExternalPackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverExternalPackages)
            *   [staleTimes](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)
            *   [staticGeneration*](https://nextjs.org/docs/app/api-reference/config/next-config-js/staticGeneration)
            *   [taint](https://nextjs.org/docs/app/api-reference/config/next-config-js/taint)
            *   [trailingSlash](https://nextjs.org/docs/app/api-reference/config/next-config-js/trailingSlash)
            *   [transpilePackages](https://nextjs.org/docs/app/api-reference/config/next-config-js/transpilePackages)
            *   [turbopack](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack)
            *   [turbopackPersistentCaching](https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopackPersistentCaching)
            *   [typedRoutes](https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes)
            *   [typescript](https://nextjs.org/docs/app/api-reference/config/next-config-js/typescript)
            *   [urlImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/urlImports)
            *   [useCache](https://nextjs.org/docs/app/api-reference/config/next-config-js/useCache)
            *   [useLightningcss](https://nextjs.org/docs/app/api-reference/config/next-config-js/useLightningcss)
            *   [viewTransition](https://nextjs.org/docs/app/api-reference/config/next-config-js/viewTransition)
            *   [webpack](https://nextjs.org/docs/app/api-reference/config/next-config-js/webpack)
            *   [webVitalsAttribution](https://nextjs.org/docs/app/api-reference/config/next-config-js/webVitalsAttribution)

        *   [TypeScript](https://nextjs.org/docs/app/api-reference/config/typescript)
        *   [ESLint](https://nextjs.org/docs/app/api-reference/config/eslint)

    *   [CLI](https://nextjs.org/docs/app/api-reference/cli)

        *   [create-next-app](https://nextjs.org/docs/app/api-reference/cli/create-next-app)
        *   [next CLI](https://nextjs.org/docs/app/api-reference/cli/next)

    *   [Edge Runtime](https://nextjs.org/docs/app/api-reference/edge)
    *   [Turbopack](https://nextjs.org/docs/app/api-reference/turbopack)

*   [Getting Started](https://nextjs.org/docs/pages/getting-started)

    *   [Installation](https://nextjs.org/docs/pages/getting-started/installation)
    *   [Project Structure](https://nextjs.org/docs/pages/getting-started/project-structure)
    *   [Images](https://nextjs.org/docs/pages/getting-started/images)
    *   [Fonts](https://nextjs.org/docs/pages/getting-started/fonts)
    *   [CSS](https://nextjs.org/docs/pages/getting-started/css)
    *   [Deploying](https://nextjs.org/docs/pages/getting-started/deploying)

*   [Guides](https://nextjs.org/docs/pages/guides)

    *   [AMP](https://nextjs.org/docs/pages/guides/amp)
    *   [Analytics](https://nextjs.org/docs/pages/guides/analytics)
    *   [Authentication](https://nextjs.org/docs/pages/guides/authentication)
    *   [Babel](https://nextjs.org/docs/pages/guides/babel)
    *   [CI Build Caching](https://nextjs.org/docs/pages/guides/ci-build-caching)
    *   [Content Security Policy](https://nextjs.org/docs/pages/guides/content-security-policy)
    *   [CSS-in-JS](https://nextjs.org/docs/pages/guides/css-in-js)
    *   [Custom Server](https://nextjs.org/docs/pages/guides/custom-server)
    *   [Debugging](https://nextjs.org/docs/pages/guides/debugging)
    *   [Draft Mode](https://nextjs.org/docs/pages/guides/draft-mode)
    *   [Environment Variables](https://nextjs.org/docs/pages/guides/environment-variables)
    *   [Forms](https://nextjs.org/docs/pages/guides/forms)
    *   [ISR](https://nextjs.org/docs/pages/guides/incremental-static-regeneration)
    *   [Instrumentation](https://nextjs.org/docs/pages/guides/instrumentation)
    *   [Internationalization](https://nextjs.org/docs/pages/guides/internationalization)
    *   [Lazy Loading](https://nextjs.org/docs/pages/guides/lazy-loading)
    *   [MDX](https://nextjs.org/docs/pages/guides/mdx)
    *   [Migrating](https://nextjs.org/docs/pages/guides/migrating)

        *   [App Router](https://nextjs.org/docs/pages/guides/migrating/app-router-migration)
        *   [Create React App](https://nextjs.org/docs/pages/guides/migrating/from-create-react-app)
        *   [Vite](https://nextjs.org/docs/pages/guides/migrating/from-vite)

    *   [Multi-Zones](https://nextjs.org/docs/pages/guides/multi-zones)
    *   [OpenTelemetry](https://nextjs.org/docs/pages/guides/open-telemetry)
    *   [Package Bundling](https://nextjs.org/docs/pages/guides/package-bundling)
    *   [PostCSS](https://nextjs.org/docs/pages/guides/post-css)
    *   [Preview Mode](https://nextjs.org/docs/pages/guides/preview-mode)
    *   [Production](https://nextjs.org/docs/pages/guides/production-checklist)
    *   [Redirecting](https://nextjs.org/docs/pages/guides/redirecting)
    *   [Sass](https://nextjs.org/docs/pages/guides/sass)
    *   [Scripts](https://nextjs.org/docs/pages/guides/scripts)
    *   [Self-Hosting](https://nextjs.org/docs/pages/guides/self-hosting)
    *   [Static Exports](https://nextjs.org/docs/pages/guides/static-exports)
    *   [Tailwind CSS](https://nextjs.org/docs/pages/guides/tailwind-v3-css)
    *   [Testing](https://nextjs.org/docs/pages/guides/testing)

        *   [Cypress](https://nextjs.org/docs/pages/guides/testing/cypress)
        *   [Jest](https://nextjs.org/docs/pages/guides/testing/jest)
        *   [Playwright](https://nextjs.org/docs/pages/guides/testing/playwright)
        *   [Vitest](https://nextjs.org/docs/pages/guides/testing/vitest)

    *   [Third Party Libraries](https://nextjs.org/docs/pages/guides/third-party-libraries)
    *   [Upgrading](https://nextjs.org/docs/pages/guides/upgrading)

        *   [Codemods](https://nextjs.org/docs/pages/guides/upgrading/codemods)
        *   [Version 10](https://nextjs.org/docs/pages/guides/upgrading/version-10)
        *   [Version 11](https://nextjs.org/docs/pages/guides/upgrading/version-11)
        *   [Version 12](https://nextjs.org/docs/pages/guides/upgrading/version-12)
        *   [Version 13](https://nextjs.org/docs/pages/guides/upgrading/version-13)
        *   [Version 14](https://nextjs.org/docs/pages/guides/upgrading/version-14)
        *   [Version 9](https://nextjs.org/docs/pages/guides/upgrading/version-9)

*   [Building Your Application](https://nextjs.org/docs/pages/building-your-application)

    *   [Routing](https://nextjs.org/docs/pages/building-your-application/routing)

        *   [Pages and Layouts](https://nextjs.org/docs/pages/building-your-application/routing/pages-and-layouts)
        *   [Dynamic Routes](https://nextjs.org/docs/pages/building-your-application/routing/dynamic-routes)
        *   [Linking and Navigating](https://nextjs.org/docs/pages/building-your-application/routing/linking-and-navigating)
        *   [Custom App](https://nextjs.org/docs/pages/building-your-application/routing/custom-app)
        *   [Custom Document](https://nextjs.org/docs/pages/building-your-application/routing/custom-document)
        *   [API Routes](https://nextjs.org/docs/pages/building-your-application/routing/api-routes)
        *   [Custom Errors](https://nextjs.org/docs/pages/building-your-application/routing/custom-error)

    *   [Rendering](https://nextjs.org/docs/pages/building-your-application/rendering)

        *   [Server-side Rendering (SSR)](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering)
        *   [Static Site Generation (SSG)](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)
        *   [Automatic Static Optimization](https://nextjs.org/docs/pages/building-your-application/rendering/automatic-static-optimization)
        *   [Client-side Rendering (CSR)](https://nextjs.org/docs/pages/building-your-application/rendering/client-side-rendering)

    *   [Data Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching)

        *   [getStaticProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-props)
        *   [getStaticPaths](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-static-paths)
        *   [Forms and Mutations](https://nextjs.org/docs/pages/building-your-application/data-fetching/forms-and-mutations)
        *   [getServerSideProps](https://nextjs.org/docs/pages/building-your-application/data-fetching/get-server-side-props)
        *   [Client-side Fetching](https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side)

    *   [Configuring](https://nextjs.org/docs/pages/building-your-application/configuring)

        *   [Error Handling](https://nextjs.org/docs/pages/building-your-application/configuring/error-handling)

*   [API Reference](https://nextjs.org/docs/pages/api-reference)

    *   [Components](https://nextjs.org/docs/pages/api-reference/components)

        *   [Font](https://nextjs.org/docs/pages/api-reference/components/font)
        *   [Form](https://nextjs.org/docs/pages/api-reference/components/form)
        *   [Head](https://nextjs.org/docs/pages/api-reference/components/head)
        *   [Image](https://nextjs.org/docs/pages/api-reference/components/image)
        *   [Image (Legacy)](https://nextjs.org/docs/pages/api-reference/components/image-legacy)
        *   [Link](https://nextjs.org/docs/pages/api-reference/components/link)
        *   [Script](https://nextjs.org/docs/pages/api-reference/components/script)

    *   [File-system conventions](https://nextjs.org/docs/pages/api-reference/file-conventions)

        *   [instrumentation.js](https://nextjs.org/docs/pages/api-reference/file-conventions/instrumentation)
        *   [Middleware](https://nextjs.org/docs/pages/api-reference/file-conventions/middleware)
        *   [public](https://nextjs.org/docs/pages/api-reference/file-conventions/public-folder)
        *   [src Directory](https://nextjs.org/docs/pages/api-reference/file-conventions/src-folder)

    *   [Functions](https://nextjs.org/docs/pages/api-reference/functions)

        *   [getInitialProps](https://nextjs.org/docs/pages/api-reference/functions/get-initial-props)
        *   [getServerSideProps](https://nextjs.org/docs/pages/api-reference/functions/get-server-side-props)
        *   [getStaticPaths](https://nextjs.org/docs/pages/api-reference/functions/get-static-paths)
        *   [getStaticProps](https://nextjs.org/docs/pages/api-reference/functions/get-static-props)
        *   [NextRequest](https://nextjs.org/docs/pages/api-reference/functions/next-request)
        *   [NextResponse](https://nextjs.org/docs/pages/api-reference/functions/next-response)
        *   [useAmp](https://nextjs.org/docs/pages/api-reference/functions/use-amp)
        *   [useReportWebVitals](https://nextjs.org/docs/pages/api-reference/functions/use-report-web-vitals)
        *   [useRouter](https://nextjs.org/docs/pages/api-reference/functions/use-router)
        *   [userAgent](https://nextjs.org/docs/pages/api-reference/functions/userAgent)

    *   [Configuration](https://nextjs.org/docs/pages/api-reference/config)

        *   [next.config.js Options](https://nextjs.org/docs/pages/api-reference/config/next-config-js)

            *   [allowedDevOrigins](https://nextjs.org/docs/pages/api-reference/config/next-config-js/allowedDevOrigins)
            *   [assetPrefix](https://nextjs.org/docs/pages/api-reference/config/next-config-js/assetPrefix)
            *   [basePath](https://nextjs.org/docs/pages/api-reference/config/next-config-js/basePath)
            *   [bundlePagesRouterDependencies](https://nextjs.org/docs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies)
            *   [compress](https://nextjs.org/docs/pages/api-reference/config/next-config-js/compress)
            *   [crossOrigin](https://nextjs.org/docs/pages/api-reference/config/next-config-js/crossOrigin)
            *   [devIndicators](https://nextjs.org/docs/pages/api-reference/config/next-config-js/devIndicators)
            *   [distDir](https://nextjs.org/docs/pages/api-reference/config/next-config-js/distDir)
            *   [env](https://nextjs.org/docs/pages/api-reference/config/next-config-js/env)
            *   [eslint](https://nextjs.org/docs/pages/api-reference/config/next-config-js/eslint)
            *   [exportPathMap](https://nextjs.org/docs/pages/api-reference/config/next-config-js/exportPathMap)
            *   [generateBuildId](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateBuildId)
            *   [generateEtags](https://nextjs.org/docs/pages/api-reference/config/next-config-js/generateEtags)
            *   [headers](https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers)
            *   [httpAgentOptions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/httpAgentOptions)
            *   [images](https://nextjs.org/docs/pages/api-reference/config/next-config-js/images)
            *   [onDemandEntries](https://nextjs.org/docs/pages/api-reference/config/next-config-js/onDemandEntries)
            *   [optimizePackageImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/optimizePackageImports)
            *   [output](https://nextjs.org/docs/pages/api-reference/config/next-config-js/output)
            *   [pageExtensions](https://nextjs.org/docs/pages/api-reference/config/next-config-js/pageExtensions)
            *   [poweredByHeader](https://nextjs.org/docs/pages/api-reference/config/next-config-js/poweredByHeader)
            *   [productionBrowserSourceMaps](https://nextjs.org/docs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps)
            *   [reactStrictMode](https://nextjs.org/docs/pages/api-reference/config/next-config-js/reactStrictMode)
            *   [redirects](https://nextjs.org/docs/pages/api-reference/config/next-config-js/redirects)
            *   [rewrites](https://nextjs.org/docs/pages/api-reference/config/next-config-js/rewrites)
            *   [Runtime Config](https://nextjs.org/docs/pages/api-reference/config/next-config-js/runtime-configuration)
            *   [serverExternalPackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/serverExternalPackages)
            *   [trailingSlash](https://nextjs.org/docs/pages/api-reference/config/next-config-js/trailingSlash)
            *   [transpilePackages](https://nextjs.org/docs/pages/api-reference/config/next-config-js/transpilePackages)
            *   [turbo](https://nextjs.org/docs/pages/api-reference/config/next-config-js/turbo)
            *   [typescript](https://nextjs.org/docs/pages/api-reference/config/next-config-js/typescript)
            *   [urlImports](https://nextjs.org/docs/pages/api-reference/config/next-config-js/urlImports)
            *   [useLightningcss](https://nextjs.org/docs/pages/api-reference/config/next-config-js/useLightningcss)
            *   [webpack](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webpack)
            *   [webVitalsAttribution](https://nextjs.org/docs/pages/api-reference/config/next-config-js/webVitalsAttribution)

        *   [TypeScript](https://nextjs.org/docs/pages/api-reference/config/typescript)
        *   [ESLint](https://nextjs.org/docs/pages/api-reference/config/eslint)

    *   [CLI](https://nextjs.org/docs/pages/api-reference/cli)

        *   [create-next-app CLI](https://nextjs.org/docs/pages/api-reference/cli/create-next-app)
        *   [next CLI](https://nextjs.org/docs/pages/api-reference/cli/next)

    *   [Edge Runtime](https://nextjs.org/docs/pages/api-reference/edge)
    *   [Turbopack](https://nextjs.org/docs/pages/api-reference/turbopack)

*   [Architecture](https://nextjs.org/docs/architecture)

    *   [Accessibility](https://nextjs.org/docs/architecture/accessibility)
    *   [Fast Refresh](https://nextjs.org/docs/architecture/fast-refresh)
    *   [Next.js Compiler](https://nextjs.org/docs/architecture/nextjs-compiler)
    *   [Supported Browsers](https://nextjs.org/docs/architecture/supported-browsers)

*   [Community](https://nextjs.org/docs/community)

    *   [Contribution Guide](https://nextjs.org/docs/community/contribution-guide)
    *   [Rspack](https://nextjs.org/docs/community/rspack)

On this page

*   [Folder and file conventions](https://nextjs.org/docs/app/getting-started/project-structure#folder-and-file-conventions)
*   [Top-level folders](https://nextjs.org/docs/app/getting-started/project-structure#top-level-folders)
*   [Top-level files](https://nextjs.org/docs/app/getting-started/project-structure#top-level-files)
*   [Routing Files](https://nextjs.org/docs/app/getting-started/project-structure#routing-files)
*   [Nested routes](https://nextjs.org/docs/app/getting-started/project-structure#nested-routes)
*   [Dynamic routes](https://nextjs.org/docs/app/getting-started/project-structure#dynamic-routes)
*   [Route Groups and private folders](https://nextjs.org/docs/app/getting-started/project-structure#route-groups-and-private-folders)
*   [Parallel and Intercepted Routes](https://nextjs.org/docs/app/getting-started/project-structure#parallel-and-intercepted-routes)
*   [Metadata file conventions](https://nextjs.org/docs/app/getting-started/project-structure#metadata-file-conventions)
*   [App icons](https://nextjs.org/docs/app/getting-started/project-structure#app-icons)
*   [Open Graph and Twitter images](https://nextjs.org/docs/app/getting-started/project-structure#open-graph-and-twitter-images)
*   [SEO](https://nextjs.org/docs/app/getting-started/project-structure#seo)
*   [Organizing your project](https://nextjs.org/docs/app/getting-started/project-structure#organizing-your-project)
*   [Component hierarchy](https://nextjs.org/docs/app/getting-started/project-structure#component-hierarchy)
*   [Colocation](https://nextjs.org/docs/app/getting-started/project-structure#colocation)
*   [Private folders](https://nextjs.org/docs/app/getting-started/project-structure#private-folders)
*   [Route groups](https://nextjs.org/docs/app/getting-started/project-structure#route-groups)
*   [src folder](https://nextjs.org/docs/app/getting-started/project-structure#src-folder)
*   [Examples](https://nextjs.org/docs/app/getting-started/project-structure#examples)
*   [Store project files outside of app](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-outside-of-app)
*   [Store project files in top-level folders inside of app](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-in-top-level-folders-inside-of-app)
*   [Split project files by feature or route](https://nextjs.org/docs/app/getting-started/project-structure#split-project-files-by-feature-or-route)
*   [Organize routes without affecting the URL path](https://nextjs.org/docs/app/getting-started/project-structure#organize-routes-without-affecting-the-url-path)
*   [Opting specific segments into a layout](https://nextjs.org/docs/app/getting-started/project-structure#opting-specific-segments-into-a-layout)
*   [Opting for loading skeletons on a specific route](https://nextjs.org/docs/app/getting-started/project-structure#opting-for-loading-skeletons-on-a-specific-route)
*   [Creating multiple root layouts](https://nextjs.org/docs/app/getting-started/project-structure#creating-multiple-root-layouts)

[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/stable/01-app/01-getting-started/02-project-structure.mdx)Scroll to top 

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Project Structure

Copy page

Project structure and organization
==================================

This page provides an overview of **all** the folder and file conventions in Next.js, and recommendations for organizing your project.

[Folder and file conventions](https://nextjs.org/docs/app/getting-started/project-structure#folder-and-file-conventions)
------------------------------------------------------------------------------------------------------------------------

### [Top-level folders](https://nextjs.org/docs/app/getting-started/project-structure#top-level-folders)

Top-level folders are used to organize your application's code and static assets.

![Image 37: Route segments to path segments](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ftop-level-folders.png&w=3840&q=75)![Image 38: Route segments to path segments](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ftop-level-folders.png&w=3840&q=75)

|  |  |
| --- | --- |
| [`app`](https://nextjs.org/docs/app) | App Router |
| [`pages`](https://nextjs.org/docs/pages/building-your-application/routing) | Pages Router |
| [`public`](https://nextjs.org/docs/app/api-reference/file-conventions/public-folder) | Static assets to be served |
| [`src`](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder) | Optional application source folder |

### [Top-level files](https://nextjs.org/docs/app/getting-started/project-structure#top-level-files)

Top-level files are used to configure your application, manage dependencies, run middleware, integrate monitoring tools, and define environment variables.

|  |  |
| --- | --- |
| **Next.js** |  |
| [`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js) | Configuration file for Next.js |
| [`package.json`](https://nextjs.org/docs/app/getting-started/installation#manual-installation) | Project dependencies and scripts |
| [`instrumentation.ts`](https://nextjs.org/docs/app/guides/instrumentation) | OpenTelemetry and Instrumentation file |
| [`middleware.ts`](https://nextjs.org/docs/app/api-reference/file-conventions/middleware) | Next.js request middleware |
| [`.env`](https://nextjs.org/docs/app/guides/environment-variables) | Environment variables |
| [`.env.local`](https://nextjs.org/docs/app/guides/environment-variables) | Local environment variables |
| [`.env.production`](https://nextjs.org/docs/app/guides/environment-variables) | Production environment variables |
| [`.env.development`](https://nextjs.org/docs/app/guides/environment-variables) | Development environment variables |
| [`.eslintrc.json`](https://nextjs.org/docs/app/api-reference/config/eslint) | Configuration file for ESLint |
| `.gitignore` | Git files and folders to ignore |
| `next-env.d.ts` | TypeScript declaration file for Next.js |
| `tsconfig.json` | Configuration file for TypeScript |
| `jsconfig.json` | Configuration file for JavaScript |

### [Routing Files](https://nextjs.org/docs/app/getting-started/project-structure#routing-files)

|  |  |  |
| --- | --- | --- |
| [`layout`](https://nextjs.org/docs/app/api-reference/file-conventions/layout) | `.js``.jsx``.tsx` | Layout |
| [`page`](https://nextjs.org/docs/app/api-reference/file-conventions/page) | `.js``.jsx``.tsx` | Page |
| [`loading`](https://nextjs.org/docs/app/api-reference/file-conventions/loading) | `.js``.jsx``.tsx` | Loading UI |
| [`not-found`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) | `.js``.jsx``.tsx` | Not found UI |
| [`error`](https://nextjs.org/docs/app/api-reference/file-conventions/error) | `.js``.jsx``.tsx` | Error UI |
| [`global-error`](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error) | `.js``.jsx``.tsx` | Global error UI |
| [`route`](https://nextjs.org/docs/app/api-reference/file-conventions/route) | `.js``.ts` | API endpoint |
| [`template`](https://nextjs.org/docs/app/api-reference/file-conventions/template) | `.js``.jsx``.tsx` | Re-rendered layout |
| [`default`](https://nextjs.org/docs/app/api-reference/file-conventions/default) | `.js``.jsx``.tsx` | Parallel route fallback page |

### [Nested routes](https://nextjs.org/docs/app/getting-started/project-structure#nested-routes)

|  |  |
| --- | --- |
| `folder` | Route segment |
| `folder/folder` | Nested route segment |

### [Dynamic routes](https://nextjs.org/docs/app/getting-started/project-structure#dynamic-routes)

|  |  |
| --- | --- |
| [`[folder]`](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#convention) | Dynamic route segment |
| [`[...folder]`](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#catch-all-segments) | Catch-all route segment |
| [`[[...folder]]`](https://nextjs.org/docs/app/api-reference/file-conventions/dynamic-routes#optional-catch-all-segments) | Optional catch-all route segment |

### [Route Groups and private folders](https://nextjs.org/docs/app/getting-started/project-structure#route-groups-and-private-folders)

|  |  |
| --- | --- |
| [`(folder)`](https://nextjs.org/docs/app/api-reference/file-conventions/route-groups#convention) | Group routes without affecting routing |
| [`_folder`](https://nextjs.org/docs/app/getting-started/project-structure#private-folders) | Opt folder and all child segments out of routing |

### [Parallel and Intercepted Routes](https://nextjs.org/docs/app/getting-started/project-structure#parallel-and-intercepted-routes)

|  |  |
| --- | --- |
| [`@folder`](https://nextjs.org/docs/app/api-reference/file-conventions/parallel-routes#slots) | Named slot |
| [`(.)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept same level |
| [`(..)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept one level above |
| [`(..)(..)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept two levels above |
| [`(...)folder`](https://nextjs.org/docs/app/api-reference/file-conventions/intercepting-routes#convention) | Intercept from root |

### [Metadata file conventions](https://nextjs.org/docs/app/getting-started/project-structure#metadata-file-conventions)

#### [App icons](https://nextjs.org/docs/app/getting-started/project-structure#app-icons)

|  |  |  |
| --- | --- | --- |
| [`favicon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#favicon) | `.ico` | Favicon file |
| [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#icon) | `.ico``.jpg``.jpeg``.png``.svg` | App Icon file |
| [`icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx) | `.js``.ts``.tsx` | Generated App Icon |
| [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#apple-icon) | `.jpg``.jpeg`, `.png` | Apple App Icon file |
| [`apple-icon`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/app-icons#generate-icons-using-code-js-ts-tsx) | `.js``.ts``.tsx` | Generated Apple App Icon |

#### [Open Graph and Twitter images](https://nextjs.org/docs/app/getting-started/project-structure#open-graph-and-twitter-images)

|  |  |  |
| --- | --- | --- |
| [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#opengraph-image) | `.jpg``.jpeg``.png``.gif` | Open Graph image file |
| [`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx) | `.js``.ts``.tsx` | Generated Open Graph image |
| [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#twitter-image) | `.jpg``.jpeg``.png``.gif` | Twitter image file |
| [`twitter-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image#generate-images-using-code-js-ts-tsx) | `.js``.ts``.tsx` | Generated Twitter image |

#### [SEO](https://nextjs.org/docs/app/getting-started/project-structure#seo)

|  |  |  |
| --- | --- | --- |
| [`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#sitemap-files-xml) | `.xml` | Sitemap file |
| [`sitemap`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap#generating-a-sitemap-using-code-js-ts) | `.js``.ts` | Generated Sitemap |
| [`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#static-robotstxt) | `.txt` | Robots file |
| [`robots`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/robots#generate-a-robots-file) | `.js``.ts` | Generated Robots file |

[Organizing your project](https://nextjs.org/docs/app/getting-started/project-structure#organizing-your-project)
----------------------------------------------------------------------------------------------------------------

Next.js is **unopinionated** about how you organize and colocate your project files. But it does provide several features to help you organize your project.

### [Component hierarchy](https://nextjs.org/docs/app/getting-started/project-structure#component-hierarchy)

The components defined in special files are rendered in a specific hierarchy:

*   `layout.js`
*   `template.js`
*   `error.js` (React error boundary)
*   `loading.js` (React suspense boundary)
*   `not-found.js` (React error boundary)
*   `page.js` or nested `layout.js`

![Image 39: Component Hierarchy for File Conventions](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Ffile-conventions-component-hierarchy.png&w=3840&q=75)![Image 40: Component Hierarchy for File Conventions](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Ffile-conventions-component-hierarchy.png&w=3840&q=75)
The components are rendered recursively in nested routes, meaning the components of a route segment will be nested **inside** the components of its parent segment.

![Image 41: Nested File Conventions Component Hierarchy](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fnested-file-conventions-component-hierarchy.png&w=3840&q=75)![Image 42: Nested File Conventions Component Hierarchy](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fnested-file-conventions-component-hierarchy.png&w=3840&q=75)
### [Colocation](https://nextjs.org/docs/app/getting-started/project-structure#colocation)

In the `app` directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.

However, even though route structure is defined through folders, a route is **not publicly accessible** until a `page.js` or `route.js` file is added to a route segment.

![Image 43: A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-not-routable.png&w=3840&q=75)![Image 44: A diagram showing how a route is not publicly accessible until a page.js or route.js file is added to a route segment.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-not-routable.png&w=3840&q=75)
And, even when a route is made publicly accessible, only the **content returned** by `page.js` or `route.js` is sent to the client.

![Image 45: A diagram showing how page.js and route.js files make routes publicly accessible.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-routable.png&w=3840&q=75)![Image 46: A diagram showing how page.js and route.js files make routes publicly accessible.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-routable.png&w=3840&q=75)
This means that **project files** can be **safely colocated** inside route segments in the `app` directory without accidentally being routable.

![Image 47: A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-colocation.png&w=3840&q=75)![Image 48: A diagram showing colocated project files are not routable even when a segment contains a page.js or route.js file.](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-colocation.png&w=3840&q=75)
> **Good to know**: While you **can** colocate your project files in `app` you don't **have** to. If you prefer, you can [keep them outside the `app` directory](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-outside-of-app).

### [Private folders](https://nextjs.org/docs/app/getting-started/project-structure#private-folders)

Private folders can be created by prefixing a folder with an underscore: `_folderName`

This indicates the folder is a private implementation detail and should not be considered by the routing system, thereby **opting the folder and all its subfolders** out of routing.

![Image 49: An example folder structure using private folders](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-private-folders.png&w=3840&q=75)![Image 50: An example folder structure using private folders](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-private-folders.png&w=3840&q=75)
Since files in the `app` directory can be [safely colocated by default](https://nextjs.org/docs/app/getting-started/project-structure#colocation), private folders are not required for colocation. However, they can be useful for:

*   Separating UI logic from routing logic.
*   Consistently organizing internal files across a project and the Next.js ecosystem.
*   Sorting and grouping files in code editors.
*   Avoiding potential naming conflicts with future Next.js file conventions.

> **Good to know**:
> 
> 
> *   While not a framework convention, you might also consider marking files outside private folders as "private" using the same underscore pattern.
> *   You can create URL segments that start with an underscore by prefixing the folder name with `%5F` (the URL-encoded form of an underscore): `%5FfolderName`.
> *   If you don't use private folders, it would be helpful to know Next.js [special file conventions](https://nextjs.org/docs/app/getting-started/project-structure#routing-files) to prevent unexpected naming conflicts.

### [Route groups](https://nextjs.org/docs/app/getting-started/project-structure#route-groups)

Route groups can be created by wrapping a folder in parenthesis: `(folderName)`

This indicates the folder is for organizational purposes and should **not be included** in the route's URL path.

![Image 51: An example folder structure using route groups](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-route-groups.png&w=3840&q=75)![Image 52: An example folder structure using route groups](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-route-groups.png&w=3840&q=75)
Route groups are useful for:

*   Organizing routes by site section, intent, or team. e.g. marketing pages, admin pages, etc.
*   Enabling nested layouts in the same route segment level:
    *   [Creating multiple nested layouts in the same segment, including multiple root layouts](https://nextjs.org/docs/app/getting-started/project-structure#creating-multiple-root-layouts)
    *   [Adding a layout to a subset of routes in a common segment](https://nextjs.org/docs/app/getting-started/project-structure#opting-specific-segments-into-a-layout)

### [`src` folder](https://nextjs.org/docs/app/getting-started/project-structure#src-folder)

Next.js supports storing application code (including `app`) inside an optional [`src` folder](https://nextjs.org/docs/app/api-reference/file-conventions/src-folder). This separates application code from project configuration files which mostly live in the root of a project.

![Image 53: An example folder structure with the `src` folder](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-src-directory.png&w=3840&q=75)![Image 54: An example folder structure with the `src` folder](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-src-directory.png&w=3840&q=75)
[Examples](https://nextjs.org/docs/app/getting-started/project-structure#examples)
----------------------------------------------------------------------------------

The following section lists a very high-level overview of common strategies. The simplest takeaway is to choose a strategy that works for you and your team and be consistent across the project.

> **Good to know**: In our examples below, we're using `components` and `lib` folders as generalized placeholders, their naming has no special framework significance and your projects might use other folders like `ui`, `utils`, `hooks`, `styles`, etc.

### [Store project files outside of `app`](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-outside-of-app)

This strategy stores all application code in shared folders in the **root of your project** and keeps the `app` directory purely for routing purposes.

![Image 55: An example folder structure with project files outside of app](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-project-root.png&w=3840&q=75)![Image 56: An example folder structure with project files outside of app](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-project-root.png&w=3840&q=75)
### [Store project files in top-level folders inside of `app`](https://nextjs.org/docs/app/getting-started/project-structure#store-project-files-in-top-level-folders-inside-of-app)

This strategy stores all application code in shared folders in the **root of the `app` directory**.

![Image 57: An example folder structure with project files inside app](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-app-root.png&w=3840&q=75)![Image 58: An example folder structure with project files inside app](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-app-root.png&w=3840&q=75)
### [Split project files by feature or route](https://nextjs.org/docs/app/getting-started/project-structure#split-project-files-by-feature-or-route)

This strategy stores globally shared application code in the root `app` directory and **splits** more specific application code into the route segments that use them.

![Image 59: An example folder structure with project files split by feature or route](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-app-root-split.png&w=3840&q=75)![Image 60: An example folder structure with project files split by feature or route](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-app-root-split.png&w=3840&q=75)
### [Organize routes without affecting the URL path](https://nextjs.org/docs/app/getting-started/project-structure#organize-routes-without-affecting-the-url-path)

To organize routes without affecting the URL, create a group to keep related routes together. The folders in parenthesis will be omitted from the URL (e.g. `(marketing)` or `(shop)`).

![Image 61: Organizing Routes with Route Groups](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-organisation.png&w=3840&q=75)![Image 62: Organizing Routes with Route Groups](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-organisation.png&w=3840&q=75)
Even though routes inside `(marketing)` and `(shop)` share the same URL hierarchy, you can create a different layout for each group by adding a `layout.js` file inside their folders.

![Image 63: Route Groups with Multiple Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-multiple-layouts.png&w=3840&q=75)![Image 64: Route Groups with Multiple Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-multiple-layouts.png&w=3840&q=75)
### [Opting specific segments into a layout](https://nextjs.org/docs/app/getting-started/project-structure#opting-specific-segments-into-a-layout)

To opt specific routes into a layout, create a new route group (e.g. `(shop)`) and move the routes that share the same layout into the group (e.g. `account` and `cart`). The routes outside of the group will not share the layout (e.g. `checkout`).

![Image 65: Route Groups with Opt-in Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-opt-in-layouts.png&w=3840&q=75)![Image 66: Route Groups with Opt-in Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-opt-in-layouts.png&w=3840&q=75)
### [Opting for loading skeletons on a specific route](https://nextjs.org/docs/app/getting-started/project-structure#opting-for-loading-skeletons-on-a-specific-route)

To apply a [loading skeleton](https://nextjs.org/docs/app/api-reference/file-conventions/loading) via a `loading.js` file to a specific route, create a new route group (e.g., `/(overview)`) and then move your `loading.tsx` inside that route group.

![Image 67: Folder structure showing a loading.tsx and a page.tsx inside the route group](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-loading.png&w=3840&q=75)![Image 68: Folder structure showing a loading.tsx and a page.tsx inside the route group](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-loading.png&w=3840&q=75)
Now, the `loading.tsx` file will only apply to your dashboard → overview page instead of all your dashboard pages without affecting the URL path structure.

### [Creating multiple root layouts](https://nextjs.org/docs/app/getting-started/project-structure#creating-multiple-root-layouts)

To create multiple [root layouts](https://nextjs.org/docs/app/api-reference/file-conventions/layout#root-layout), remove the top-level `layout.js` file, and add a `layout.js` file inside each route group. This is useful for partitioning an application into sections that have a completely different UI or experience. The `<html>` and `<body>` tags need to be added to each root layout.

![Image 69: Route Groups with Multiple Root Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Froute-group-multiple-root-layouts.png&w=3840&q=75)![Image 70: Route Groups with Multiple Root Layouts](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Froute-group-multiple-root-layouts.png&w=3840&q=75)
In the example above, both `(marketing)` and `(shop)` have their own root layout.

[Previous Installation](https://nextjs.org/docs/app/getting-started/installation)[Next Layouts and Pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)

Was this helpful?

supported.

Send

[](https://vercel.com/home?utm_source=next-site&utm_medium=footer&utm_campaign=next-website "Go to the Vercel website")

[](https://github.com/vercel/next.js)

* * *

[](https://x.com/nextjs)

* * *

[](https://bsky.app/profile/nextjs.org)

#### Resources

[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Analytics](https://vercel.com/analytics?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_project-structure)[Next.js Conf](https://nextjs.org/conf)[Previews](https://vercel.com/products/previews?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_project-structure)

#### More

[Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_project-structure)[Contact Sales](https://vercel.com/contact/sales?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_project-structure)[Community](https://community.vercel.com/)[GitHub](https://github.com/vercel/next.js)[Releases](https://github.com/vercel/next.js/releases)[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)

#### About Vercel

[Next.js + Vercel](https://vercel.com/solutions/nextjs?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_project-structure)[Open Source Software](https://vercel.com/oss?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_project-structure)[GitHub](https://github.com/vercel)[Bluesky](https://bsky.app/profile/vercel.com)[X](https://x.com/vercel)

#### Legal

[Privacy Policy](https://vercel.com/legal/privacy-policy)Cookie Preferences

#### Subscribe to our newsletter

Stay updated on new releases and features, guides, and case studies.

Subscribe

© 2025 Vercel, Inc.

[](https://github.com/vercel/next.js)

* * *

[](https://x.com/nextjs)

* * *

[](https://bsky.app/profile/nextjs.org)
