Title: Getting Started: Error Handling

URL Source: https://nextjs.org/docs/app/building-your-application/routing/error-handling

Markdown Content:
Getting Started: Error Handling | Next.js

===============
[Skip to content](https://nextjs.org/docs/app/building-your-application/routing/error-handling#geist-skip-nav)

[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_app_getting-started_error-handling "Go to Vercel homepage")

[![Image 3: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true "Go to the homepage")

[](https://nextjs.org/ "Go to the homepage")

Search documentation...CtrlK Search...⌘K

[](https://vercel.com/home?utm_source=next-site&utm_medium=banner&utm_campaign=docs_app_getting-started_error-handling "Go to Vercel homepage")

[![Image 4: Next.js uwu logo by SAWARATSUKI](https://nextjs.org/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1714730590%2Ffront%2Fnextjs%2Fuwu%2Fnext-uwu-logo.png&w=128&q=75)](https://nextjs.org/?uwu=true "Go to the homepage")

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

*   [Handling expected errors](https://nextjs.org/docs/app/building-your-application/routing/error-handling#handling-expected-errors)
*   [Server Functions](https://nextjs.org/docs/app/building-your-application/routing/error-handling#server-functions)
*   [Server Components](https://nextjs.org/docs/app/building-your-application/routing/error-handling#server-components)
*   [Not found](https://nextjs.org/docs/app/building-your-application/routing/error-handling#not-found)
*   [Handling uncaught exceptions](https://nextjs.org/docs/app/building-your-application/routing/error-handling#handling-uncaught-exceptions)
*   [Nested error boundaries](https://nextjs.org/docs/app/building-your-application/routing/error-handling#nested-error-boundaries)
*   [Global errors](https://nextjs.org/docs/app/building-your-application/routing/error-handling#global-errors)
*   [API Reference](https://nextjs.org/docs/app/building-your-application/routing/error-handling#api-reference)

[Edit this page on GitHub](https://github.com/vercel/next.js/edit/canary/docs/stable/01-app/01-getting-started/10-error-handling.mdx)Scroll to top 

[App Router](https://nextjs.org/docs/app)[Getting Started](https://nextjs.org/docs/app/getting-started)Error Handling

Copy page

Error Handling
==============

Errors can be divided into two categories: [expected errors](https://nextjs.org/docs/app/building-your-application/routing/error-handling#handling-expected-errors) and [uncaught exceptions](https://nextjs.org/docs/app/building-your-application/routing/error-handling#handling-uncaught-exceptions). This page will walk you through how you can handle these errors in your Next.js application.

[Handling expected errors](https://nextjs.org/docs/app/building-your-application/routing/error-handling#handling-expected-errors)
---------------------------------------------------------------------------------------------------------------------------------

Expected errors are those that can occur during the normal operation of the application, such as those from [server-side form validation](https://nextjs.org/docs/app/guides/forms) or failed requests. These errors should be handled explicitly and returned to the client.

### [Server Functions](https://nextjs.org/docs/app/building-your-application/routing/error-handling#server-functions)

You can use the [`useActionState`](https://react.dev/reference/react/useActionState) hook to handle expected errors in [Server Functions](https://react.dev/reference/rsc/server-functions).

For these errors, avoid using `try`/`catch` blocks and throw errors. Instead, model expected errors as return values.

app/actions.ts

TypeScript

```
'use server'
 
export async function createPost(prevState: any, formData: FormData) {
  const title = formData.get('title')
  const content = formData.get('content')
 
  const res = await fetch('https://api.vercel.app/posts', {
    method: 'POST',
    body: { title, content },
  })
  const json = await res.json()
 
  if (!res.ok) {
    return { message: 'Failed to create post' }
  }
}
```

You can pass your action to the `useActionState` hook and use the returned `state` to display an error message.

app/ui/form.tsx

TypeScript

```
'use client'
 
import { useActionState } from 'react'
import { createPost } from '@/app/actions'
 
const initialState = {
  message: '',
}
 
export function Form() {
  const [state, formAction, pending] = useActionState(createPost, initialState)
 
  return (
    <form action={formAction}>
      <label htmlFor="title">Title</label>
      <input type="text" id="title" name="title" required />
      <label htmlFor="content">Content</label>
      <textarea id="content" name="content" required />
      {state?.message && <p aria-live="polite">{state.message}</p>}
      <button disabled={pending}>Create Post</button>
    </form>
  )
}
```

### [Server Components](https://nextjs.org/docs/app/building-your-application/routing/error-handling#server-components)

When fetching data inside of a Server Component, you can use the response to conditionally render an error message or [`redirect`](https://nextjs.org/docs/app/api-reference/functions/redirect).

app/page.tsx

TypeScript

```
export default async function Page() {
  const res = await fetch(`https://...`)
  const data = await res.json()
 
  if (!res.ok) {
    return 'There was an error.'
  }
 
  return '...'
}
```

### [Not found](https://nextjs.org/docs/app/building-your-application/routing/error-handling#not-found)

You can call the [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) function within a route segment and use the [`not-found.js`](https://nextjs.org/docs/app/api-reference/file-conventions/not-found) file to show a 404 UI.

app/blog/[slug]/page.tsx

TypeScript

```
import { getPostBySlug } from '@/lib/posts'
 
export default async function Page({ params }: { params: { slug: string } }) {
  const { slug } = await params
  const post = getPostBySlug(slug)
 
  if (!post) {
    notFound()
  }
 
  return <div>{post.title}</div>
}
```

app/blog/[slug]/not-found.tsx

TypeScript

```
export default function NotFound() {
  return <div>404 - Page Not Found</div>
}
```

[Handling uncaught exceptions](https://nextjs.org/docs/app/building-your-application/routing/error-handling#handling-uncaught-exceptions)
-----------------------------------------------------------------------------------------------------------------------------------------

Uncaught exceptions are unexpected errors that indicate bugs or issues that should not occur during the normal flow of your application. These should be handled by throwing errors, which will then be caught by error boundaries.

### [Nested error boundaries](https://nextjs.org/docs/app/building-your-application/routing/error-handling#nested-error-boundaries)

Next.js uses error boundaries to handle uncaught exceptions. Error boundaries catch errors in their child components and display a fallback UI instead of the component tree that crashed.

Create an error boundary by adding an [`error.js`](https://nextjs.org/docs/app/api-reference/file-conventions/error) file inside a route segment and exporting a React component:

app/dashboard/error.tsx

TypeScript

```
'use client' // Error boundaries must be Client Components
 
import { useEffect } from 'react'
 
export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error)
  }, [error])
 
  return (
    <div>
      <h2>Something went wrong!</h2>
      <button
        onClick={
          // Attempt to recover by trying to re-render the segment
          () => reset()
        }
      >
        Try again
      </button>
    </div>
  )
}
```

Errors will bubble up to the nearest parent error boundary. This allows for granular error handling by placing `error.tsx` files at different levels in the [route hierarchy](https://nextjs.org/docs/app/getting-started/project-structure#component-hierarchy).

![Image 5: Nested Error Component Hierarchy](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fnested-error-component-hierarchy.png&w=3840&q=75)![Image 6: Nested Error Component Hierarchy](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fnested-error-component-hierarchy.png&w=3840&q=75)
Error boundaries don’t catch errors inside event handlers. They’re designed to catch errors [during rendering](https://react.dev/reference/react/Component#static-getderivedstatefromerror) to show a **fallback UI** instead of crashing the whole app.

In general, errors in event handlers or async code aren’t handled by error boundaries because they run after rendering.

To handle these cases, catch the error manually and store it using `useState` or `useReducer`, then update the UI to inform the user.

```
'use client'
 
import { useState } from 'react'
 
export function Button() {
  const [error, setError] = useState(null)
 
  const handleClick = () => {
    try {
      // do some work that might fail
      throw new Error('Exception')
    } catch (reason) {
      setError(reason)
    }
  }
 
  if (error) {
    /* render fallback UI */
  }
 
  return (
    <button type="button" onClick={handleClick}>
      Click me
    </button>
  )
}
```

Note that unhandled errors inside `startTransition` from `useTransition`, will bubble up to the nearest error boundary.

```
'use client'
 
import { useTransition } from 'react'
 
export function Button() {
  const [pending, startTransition] = useTransition()
 
  const handleClick = () =>
    startTransition(() => {
      throw new Error('Exception')
    })
 
  return (
    <button type="button" onClick={handleClick}>
      Click me
    </button>
  )
}
```

### [Global errors](https://nextjs.org/docs/app/building-your-application/routing/error-handling#global-errors)

While less common, you can handle errors in the root layout using the [`global-error.js`](https://nextjs.org/docs/app/api-reference/file-conventions/error#global-error) file, located in the root app directory, even when leveraging [internationalization](https://nextjs.org/docs/app/guides/internationalization). Global error UI must define its own `<html>` and `<body>` tags, since it is replacing the root layout or template when active.

app/global-error.tsx

TypeScript

```
'use client' // Error boundaries must be Client Components
 
export default function GlobalError({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    // global-error must include html and body tags
    <html>
      <body>
        <h2>Something went wrong!</h2>
        <button onClick={() => reset()}>Try again</button>
      </body>
    </html>
  )
}
```

API Reference
-------------

Learn more about the features mentioned in this page by reading the API Reference.

[### redirect API Reference for the redirect function.](https://nextjs.org/docs/app/api-reference/functions/redirect)[### error.js API reference for the error.js special file.](https://nextjs.org/docs/app/api-reference/file-conventions/error)[### notFound API Reference for the notFound function.](https://nextjs.org/docs/app/api-reference/functions/not-found)[### not-found.js API reference for the not-found.js file.](https://nextjs.org/docs/app/api-reference/file-conventions/not-found)

[Previous Caching and Revalidating](https://nextjs.org/docs/app/getting-started/caching-and-revalidating)[Next CSS](https://nextjs.org/docs/app/getting-started/css)

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

[Docs](https://nextjs.org/docs)[Support Policy](https://nextjs.org/support-policy)[Learn](https://nextjs.org/learn)[Showcase](https://nextjs.org/showcase)[Blog](https://nextjs.org/blog)[Team](https://nextjs.org/team)[Analytics](https://vercel.com/analytics?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_error-handling)[Next.js Conf](https://nextjs.org/conf)[Previews](https://vercel.com/products/previews?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_error-handling)

#### More

[Next.js Commerce](https://vercel.com/templates/next.js/nextjs-commerce?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_error-handling)[Contact Sales](https://vercel.com/contact/sales?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_error-handling)[Community](https://community.vercel.com/)[GitHub](https://github.com/vercel/next.js)[Releases](https://github.com/vercel/next.js/releases)[Telemetry](https://nextjs.org/telemetry)[Governance](https://nextjs.org/governance)

#### About Vercel

[Next.js + Vercel](https://vercel.com/solutions/nextjs?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_error-handling)[Open Source Software](https://vercel.com/oss?utm_source=next-site&utm_medium=footer&utm_campaign=docs_app_getting-started_error-handling)[GitHub](https://github.com/vercel)[Bluesky](https://bsky.app/profile/vercel.com)[X](https://x.com/vercel)

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
