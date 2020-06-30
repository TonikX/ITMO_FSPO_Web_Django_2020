import React, {useContext, useState} from "react";
import {AuthContext} from "../context/auth";
import {Login, Logout} from "./auth";

export const Home = () => {
    const auth = useContext(AuthContext)
    console.log('home', auth.token)

    if (!!auth.token) {
       return(
            <div>
                <a href="/trip">Прокатимся?</a>
            </div>
        )
    } else {
        return (
            <Login />
        )
    }
}
