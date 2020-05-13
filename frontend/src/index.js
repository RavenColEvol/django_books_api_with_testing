import React from 'react'
import ReactDOM from 'react-dom'
import {Provider} from 'react-redux'

import Layout from './components/Layout'
import store from './redux/store'

const App = () => {
    return (
        <Provider store={store}>
            <Layout/>
        </Provider>
    )
}

ReactDOM.render(<App/>, document.getElementById('app'))