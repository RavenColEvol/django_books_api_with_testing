import React, {useEffect, useState} from 'react'

export default function Book() {

    useEffect(() => {
        fetch('/api/books')
        .then(res => res.json())
        .then(res => setBooks(res['results']) )
    }, [])

    const [books, setBooks] = useState([]);

    return (
        <div>
            {
                books.map(e => (
                    <div className="card" style={{"width":"18rem"}} key={e.id}>
                        <a href={`/#/${e.slug}`}>See</a>
                        <img src={e.image} className="card-img-top" alt="..." />
                        <div className="card-body">
                            <h5 className="card-title">{e.title}</h5>
                            <p className="card-text">{e.description}</p>
                        </div>
                    </div>
                ))
            }
        </div>
    )
}
