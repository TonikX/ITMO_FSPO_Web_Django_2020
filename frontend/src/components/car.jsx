import React, {useEffect, useState} from "react";
import {useHttp} from "../hooks/http.hook";

export const Car = (props) => {
    const [car, setCar] = useState({name: "Не найдена", price: "Выгодная", found: false})
    const {request} = useHttp()

    useEffect(() => {
        request('/api/car/' + props.match.params.id)
            .then(data => setCar({...data, found: true}))
            .catch(e => console.log(e))
    }, [props.match.params.id, request])

    return (
        <div>
            <h1>{car.name}</h1>
            <p>Цена за минуту: {car.price}</p>
            {car.found && <a href={"/request/repair/" + car.name}>Заметил поломку</a>}
        </div>
    )
}