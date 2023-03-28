import React, {Usecontext, UseState} from 'react'
import { Layout } from '@/components'

import 'tailwindcss/tailwind.css'
import '../styles/globals.scss'
// import '@/styles/globals.css'

export default function App({ Component, pageProps }) {
  return (
    <>
      <Layout>
      <Component {...pageProps} />
      </Layout>
    </>
  )
}
