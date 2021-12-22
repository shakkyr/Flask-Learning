import React from 'react'
import { List , Header, Rating } from 'semantic-ui-react';

const Movies = ({movies}) => {
    console.log(movies);
    return (
        <div>
            <List>
                {movies.map(ele=>{
                    return (
                        <List.Item key={ele.title} >
                            <Header >
                                {ele.title}
                            </Header>   
                            <Rating rating={ele.rating} maxRating={5} disabled />
                        </List.Item>
                        )
                })}
            </List>
        </div>
    )
}

export default Movies
