import React from 'react'
import {HashRouter as Router, Switch, Route} from 'react-router-dom'

import Book from './Book'

export default () => {
    return (
        <Router>
            <Switch>
                <Route path='/' exact>
                    <Book/>
                </Route>
                <Route path='/:slug' exact>
                    <h1>Book</h1>
                </Route>
            </Switch>
        </Router>
    )
}