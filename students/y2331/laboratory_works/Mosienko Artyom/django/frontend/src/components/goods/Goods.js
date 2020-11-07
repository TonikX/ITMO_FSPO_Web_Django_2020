import React from "react";
import Tabulator from "tabulator-tables";

class Goods extends React.Component {
    el = React.createRef();

    tabulator = null; //variable to hold your table
    tableData = ["fdfsdfdsmf", "fdfsdfdsmf"]; //data for table to display

    componentDidMount() {
        //instantiate Tabulator when element is mounted
        this.tabulator = new Tabulator(this.el, {
            data: this.tableData, //link data to table
            columns: [
            {title:"Name", field:"name", width:150},
            {title:"Age", field:"age"},
            {title:"Sex", field:"sex"},
            {title:"Info", field:"info",editor:"input"},
        ] //define table columns
        });
    }

    //add table holder element to DOM
    render(){
        return (
            <div>
                <p>
                    Test
                </p>
                <div ref={el => (this.el = el)} />
            </div>
            );
    }
}

export default Goods;