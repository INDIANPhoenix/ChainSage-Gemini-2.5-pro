Title: Getting Started: Server and Client Components

URL Source: https://nextjs.org/docs/app/building-your-application/rendering/server-components

Markdown Content:
Getting Started: Server and Client Components | Next.js

===============
[Skip to content](https://nextjs.org/docs/app/building-your-application/rendering/server-components#geist-skip-nav)

[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_app_getting-started_server-and-client-components "Go to Vercel homepage")

[![Image 1: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true "Go to the homepage")

[](https://nextjs.org/ "Go to the homepage")

Search documentation...CtrlK Search...⌘K

[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_app_getting-started_server-and-client-components "Go to Vercel homepage")

[![Image 2: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true "Go to the homepage")

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

*   [When to use Server and Client Components?](https://nextjs.org/docs/app/building-your-application/rendering/server-components#when-to-use-server-and-client-components)
*   [How do Server and Client Components work in Next.js?](https://nextjs.org/docs/app/building-your-application/rendering/server-components#how-do-server-and-client-components-work-in-nextjs)
*   [On the server](https://nextjs.org/docs/app/building-your-application/rendering/server-components#on-the-server)
*   [On the client (first load)](https://nextjs.org/docs/app/building-your-application/rendering/server-components#on-the-client-first-load)
*   [Subsequent Navigations](https://nextjs.org/docs/app/building-your-application/rendering/server-components#subsequent-navigations)
*   [Examples](https://nextjs.org/docs/app/building-your-application/rendering/server-components#examples)
*   [Using Client Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components#using-client-components)
*   [Reducing JS bundle size](https://nextjs.org/docs/app/building-your-application/rendering/server-components#reducing-js-bundle-size)
*   [Passing data from Server to Client Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components#passing-data-from-server-to-client-components)
*   [Interleaving Server and Client Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components#interleaving-server-and-client-components)
*   [Context providers](https://nextjs.org/docs/app/building-your-application/rendering/server-components#context-providers)
*   [Third-party components](https://nextjs.org/docs/app/building-your-application/rendering/server-components#third-party-components)
*   [Preventing environment poisoning](https://nextjs.org/docs/app/building-your-application/rendering/server-components#preventing-environment-poisoning)
*   [Next Steps](https://nextjs.org/docs/app/building-your-application/rendering/server-components#next-steps)

[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/stable/01-app/01-getting-started/05-server-and-client-components.mdx)Scroll to top 

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Server and Client Components

Copy page

Server and Client Components
============================

By default, layouts and pages are [Server Components](https://react.dev/reference/rsc/server-components), which lets you fetch data and render parts of your UI on the server, optionally cache the result, and stream it to the client. When you need interactivity or browser APIs, you can use [Client Components](https://react.dev/reference/rsc/use-client) to layer in functionality.

This page explains how Server and Client Components work in Next.js and when to use them, with examples of how to compose them together in your application.

[When to use Server and Client Components?](https://nextjs.org/docs/app/building-your-application/rendering/server-components#when-to-use-server-and-client-components)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The client and server environments have different capabilities. Server and Client components allow you to run logic in each environment depending on your use case.

Use **Client Components** when you need:

*   [State](https://react.dev/learn/managing-state) and [event handlers](https://react.dev/learn/responding-to-events). E.g. `onClick`, `onChange`.
*   [Lifecycle logic](https://react.dev/learn/lifecycle-of-reactive-effects). E.g. `useEffect`.
*   Browser-only APIs. E.g. `localStorage`, `window`, `Navigator.geolocation`, etc.
*   [Custom hooks](https://react.dev/learn/reusing-logic-with-custom-hooks).

Use **Server Components** when you need:

*   Fetch data from databases or APIs close to the source.
*   Use API keys, tokens, and other secrets without exposing them to the client.
*   Reduce the amount of JavaScript sent to the browser.
*   Improve the [First Contentful Paint (FCP)](https://web.dev/fcp/), and stream content progressively to the client.

For example, the `<Page>` component is a Server Component that fetches data about a post, and passes it as props to the `<LikeButton>` which handles client-side interactivity.

app/[id]/page.tsx

TypeScript

```
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'
 
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post = await getPost(id)
 
  return (
    <div>
      <main>
        <h1>{post.title}</h1>
        {/* ... */}
        <LikeButton likes={post.likes} />
      </main>
    </div>
  )
}
```

app/ui/like-button.tsx

TypeScript

```
'use client'
 
import { useState } from 'react'
 
export default function LikeButton({ likes }: { likes: number }) {
  // ...
}
```

[How do Server and Client Components work in Next.js?](https://nextjs.org/docs/app/building-your-application/rendering/server-components#how-do-server-and-client-components-work-in-nextjs)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [On the server](https://nextjs.org/docs/app/building-your-application/rendering/server-components#on-the-server)

On the server, Next.js uses React's APIs to orchestrate rendering. The rendering work is split into chunks, by individual route segments ([layouts and pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages)):

*   **Server Components** are rendered into a special data format called the React Server Component Payload (RSC Payload).
*   **Client Components** and the RSC Payload are used to [prerender](https://nextjs.org/docs/app/getting-started/partial-prerendering#how-does-partial-prerendering-work) HTML.

> **What is the React Server Component Payload (RSC)?**
> 
> 
> The RSC Payload is a compact binary representation of the rendered React Server Components tree. It's used by React on the client to update the browser's DOM. The RSC Payload contains:
> 
> 
> *   The rendered result of Server Components
> *   Placeholders for where Client Components should be rendered and references to their JavaScript files
> *   Any props passed from a Server Component to a Client Component

### [On the client (first load)](https://nextjs.org/docs/app/building-your-application/rendering/server-components#on-the-client-first-load)

Then, on the client:

1.   **HTML** is used to immediately show a fast non-interactive preview of the route to the user.
2.   **RSC Payload** is used to reconcile the Client and Server Component trees.
3.   **JavaScript** is used to hydrate Client Components and make the application interactive.

> **What is hydration?**
> 
> 
> Hydration is React's process for attaching [event handlers](https://react.dev/learn/responding-to-events) to the DOM, to make the static HTML interactive.

### [Subsequent Navigations](https://nextjs.org/docs/app/building-your-application/rendering/server-components#subsequent-navigations)

On subsequent navigations:

*   The **RSC Payload** is prefetched and cached for instant navigation.
*   **Client Components** are rendered entirely on the client, without the server-rendered HTML.

[Examples](https://nextjs.org/docs/app/building-your-application/rendering/server-components#examples)
------------------------------------------------------------------------------------------------------

### [Using Client Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components#using-client-components)

You can create a Client Component by adding the [`"use client"`](https://react.dev/reference/react/use-client) directive at the top of the file, above your imports.

app/ui/counter.tsx

TypeScript

```
'use client'
 
import { useState } from 'react'
 
export default function Counter() {
  const [count, setCount] = useState(0)
 
  return (
    <div>
      <p>{count} likes</p>
      <button onClick={() => setCount(count + 1)}>Click me</button>
    </div>
  )
}
```

`"use client"` is used to declare a **boundary** between the Server and Client module graphs (trees).

Once a file is marked with `"use client"`, **all its imports and child components are considered part of the client bundle**. This means you don't need to add the directive to every component that is intended for the client.

### [Reducing JS bundle size](https://nextjs.org/docs/app/building-your-application/rendering/server-components#reducing-js-bundle-size)

To reduce the size of your client JavaScript bundles, add `'use client'` to specific interactive components instead of marking large parts of your UI as Client Components.

For example, the `<Layout>` component contains mostly static elements like a logo and navigation links, but includes an interactive search bar. `<Search />` is interactive and needs to be a Client Component, however, the rest of the layout can remain a Server Component.

app/layout.tsx

TypeScript

```
// Client Component
import Search from './search'
// Server Component
import Logo from './logo'
 
// Layout is a Server Component by default
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <nav>
        <Logo />
        <Search />
      </nav>
      <main>{children}</main>
    </>
  )
}
```

app/ui/search.tsx

TypeScript

```
'use client'
 
export default function Search() {
  // ...
}
```

### [Passing data from Server to Client Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components#passing-data-from-server-to-client-components)

You can pass data from Server Components to Client Components using props.

app/[id]/page.tsx

TypeScript

```
import LikeButton from '@/app/ui/like-button'
import { getPost } from '@/lib/data'
 
export default async function Page({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const post = await getPost(id)
 
  return <LikeButton likes={post.likes} />
}
```

app/ui/like-button.tsx

TypeScript

```
'use client'
 
export default function LikeButton({ likes }: { likes: number }) {
  // ...
}
```

Alternatively, you can stream data from a Server Component to a Client Component with the [`use` Hook](https://react.dev/reference/react/use). See an [example](https://nextjs.org/docs/app/getting-started/fetching-data#streaming-data-with-the-use-hook).

> **Good to know**: Props passed to Client Components need to be [serializable](https://react.dev/reference/react/use-server#serializable-parameters-and-return-values) by React.

### [Interleaving Server and Client Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components#interleaving-server-and-client-components)

You can pass Server Components as a prop to a Client Component. This allows you to visually nest server-rendered UI within Client components.

A common pattern is to use `children` to create a _slot_ in a `<ClientComponent>`. For example, a `<Cart>` component that fetches data on the server, inside a `<Modal>` component that uses client state to toggle visibility.

app/ui/modal.tsx

TypeScript

```
'use client'
 
export default function Modal({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>
}
```

Then, in a parent Server Component (e.g.`<Page>`), you can pass a `<Cart>` as the child of the `<Modal>`:

app/page.tsx

TypeScript

```
import Modal from './ui/modal'
import Cart from './ui/cart'
 
export default function Page() {
  return (
    <Modal>
      <Cart />
    </Modal>
  )
}
```

In this pattern, all Server Components will be rendered on the server ahead of time, including those as props. The resulting RSC payload will contain references of where Client Components should be rendered within the component tree.

### [Context providers](https://nextjs.org/docs/app/building-your-application/rendering/server-components#context-providers)

[React context](https://react.dev/learn/passing-data-deeply-with-context) is commonly used to share global state like the current theme. However, React context is not supported in Server Components.

To use context, create a Client Component that accepts `children`:

app/theme-provider.tsx

TypeScript

```
'use client'
 
import { createContext } from 'react'
 
export const ThemeContext = createContext({})
 
export default function ThemeProvider({
  children,
}: {
  children: React.ReactNode
}) {
  return <ThemeContext.Provider value="dark">{children}</ThemeContext.Provider>
}
```

Then, import it into a Server Component (e.g. `layout`):

app/layout.tsx

TypeScript

```
import ThemeProvider from './theme-provider'
 
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html>
      <body>
        <ThemeProvider>{children}</ThemeProvider>
      </body>
    </html>
  )
}
```

Your Server Component will now be able to directly render your provider, and all other Client Components throughout your app will be able to consume this context.

> **Good to know**: You should render providers as deep as possible in the tree – notice how `ThemeProvider` only wraps `{children}` instead of the entire `<html>` document. This makes it easier for Next.js to optimize the static parts of your Server Components.

### [Third-party components](https://nextjs.org/docs/app/building-your-application/rendering/server-components#third-party-components)

When using a third-party component that relies on client-only features, you can wrap it in a Client Component to ensure it works as expected.

For example, the `<Carousel />` can be imported from the `acme-carousel` package. This component uses `useState`, but it doesn't yet have the `"use client"` directive.

If you use `<Carousel />` within a Client Component, it will work as expected:

app/gallery.tsx

TypeScript

```
'use client'
 
import { useState } from 'react'
import { Carousel } from 'acme-carousel'
 
export default function Gallery() {
  const [isOpen, setIsOpen] = useState(false)
 
  return (
    <div>
      <button onClick={() => setIsOpen(true)}>View pictures</button>
      {/* Works, since Carousel is used within a Client Component */}
      {isOpen && <Carousel />}
    </div>
  )
}
```

However, if you try to use it directly within a Server Component, you'll see an error. This is because Next.js doesn't know `<Carousel />` is using client-only features.

To fix this, you can wrap third-party components that rely on client-only features in your own Client Components:

app/carousel.tsx

TypeScript

```
'use client'
 
import { Carousel } from 'acme-carousel'
 
export default Carousel
```

Now, you can use `<Carousel />` directly within a Server Component:

app/page.tsx

TypeScript

```
import Carousel from './carousel'
 
export default function Page() {
  return (
    <div>
      <p>View pictures</p>
      {/*  Works, since Carousel is a Client Component */}
      <Carousel />
    </div>
  )
}
```

> **Advice for Library Authors**
> 
> 
> If you’re building a component library, add the `"use client"` directive to entry points that rely on client-only features. This lets your users import components into Server Components without needing to create wrappers.
> 
> 
> It's worth noting some bundlers might strip out `"use client"` directives. You can find an example of how to configure esbuild to include the `"use client"` directive in the [React Wrap Balancer](https://github.com/shuding/react-wrap-balancer/blob/main/tsup.config.ts#L10-L13) and [Vercel Analytics](https://github.com/vercel/analytics/blob/main/packages/web/tsup.config.js#L26-L30) repositories.

### [Preventing environment poisoning](https://nextjs.org/docs/app/building-your-application/rendering/server-components#preventing-environment-poisoning)

JavaScript modules can be shared between both Server and Client Components modules. This means it's possible to accidentally import server-only code into the client. For example, consider the following function:

lib/data.ts

TypeScript

```
export async function getData() {
  const res = await fetch('https://external-service.com/data', {
    headers: {
      authorization: process.env.API_KEY,
    },
  })
 
  return res.json()
}
```

This function contains an `API_KEY` that should never be exposed to the client.

In Next.js, only environment variables prefixed with `NEXT_PUBLIC_` are included in the client bundle. If variables are not prefixed, Next.js replaces them with an empty string.

As a result, even though `getData()` can be imported and executed on the client, it won't work as expected.

To prevent accidental usage in Client Components, you can use the [`server-only` package](https://www.npmjs.com/package/server-only).

Then, import the package into a file that contains server-only code:

lib/data.js

```
import 'server-only'
 
export async function getData() {
  const res = await fetch('https://external-service.com/data', {
    headers: {
      authorization: process.env.API_KEY,
    },
  })
 
  return res.json()
}
```

Now, if you try to import the module into a Client Component, there will be a build-time error.

The corresponding [`client-only` package](https://www.npmjs.com/package/client-only) can be used to mark modules that contain client-only logic like code that accesses the `window` object.

In Next.js, installing `server-only` or `client-only` is **optional**. However, if your linting rules flag extraneous dependencies, you may install them to avoid issues.

pnpm npm yarn bun

Terminal

`pnpm add server-only`

Next.js handles `server-only` and `client-only` imports internally to provide clearer error messages when a module is used in the wrong environment. The contents of these packages from NPM are not used by Next.js.

Next.js also provides its own type declarations for `server-only` and `client-only`, for TypeScript configurations where [`noUncheckedSideEffectImports`](https://www.typescriptlang.org/tsconfig/#noUncheckedSideEffectImports) is active.

Next Steps
----------

Learn more about the APIs mentioned in this page.

[### use client Learn how to use the use client directive to render a component on the client.](https://nextjs.org/docs/app/api-reference/directives/use-client)

[Previous Linking and Navigating](https://nextjs.org/docs/app/getting-started/linking-and-navigating)[Next Partial Prerendering](https://nextjs.org/docs/app/getting-started/partial-prerendering)

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

[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Analytics](https://vercel.com/analytics?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_server-and-client-components)[Next.js Conf](https://nextjs.org/conf)[Previews](https://vercel.com/products/previews?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_server-and-client-components)

#### More

[Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_server-and-client-components)[Contact Sales](https://vercel.com/contact/sales?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_server-and-client-components)[Community](https://community.vercel.com/)[GitHub](https://github.com/vercel/next.js)[Releases](https://github.com/vercel/next.js/releases)[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)

#### About Vercel

[Next.js + Vercel](https://vercel.com/solutions/nextjs?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_server-and-client-components)[Open Source Software](https://vercel.com/oss?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_server-and-client-components)[GitHub](https://github.com/vercel)[Bluesky](https://bsky.app/profile/vercel.com)[X](https://x.com/vercel)

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
