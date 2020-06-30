import React, {useState} from "react";
import {useHttp} from "../hooks/http.hook";

export const Car = (props) => {
    const [car, setCar] = useState({name: "Не найдена"})
    const {request} = useHttp()

    //  useEffect(() => {
    //     request('/api//' + props.match.params.id)
    //         .then(data => setDonation(data))
    //         .catch(() => { })
    // }, [props, request])

}