import './App.css';
import React from "react";
import {Route, BrowserRouter, NavLink} from "react-router-dom";
import Client from "./components/Client/Client";
import Goods from "./components/goods/Goods"

function App() {
  return (
    <BrowserRouter>
      <div className={"app"}>
        <header>
          <nav>
            <NavLink to={"/client"}>Клиенты</NavLink>
            <NavLink to={"/transactions"}>Транзакции</NavLink>
            <NavLink to={"/cards"}>Дисконтные карты</NavLink>
            <NavLink to={"/goods"}>Товары</NavLink>
            <NavLink to={"/sold"}>Проданные товары</NavLink>
            <NavLink to={"/visit"}>Посещения</NavLink>
            <NavLink to={"/provided"}>Проведённые услуги</NavLink>
            <NavLink to={"/services"}>Услуги</NavLink>
          </nav>
        </header>
        <div className={"main"}>
          <Route path='/client' component={Client}/>
          <Route path='/goods' component={Goods}/>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
