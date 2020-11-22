import React from 'react';
import {BrowserRouter} from "react-router-dom";
import s from "./Client.module.css";
import axios from "axios";
import Modal from "./Modal";

let Client_obj = {
  id: null,
  passport_id: "",
  full_name: "",
  birth_date: "",
  address_registration: "",
  address_residence: "",
  occupation: "",
  phones: "",
  gender: "",
  birth_place: "",
  discovery_info: "",
  email: "",
  comment: "",
  comment_addition: "",
  balance: null,
  permanent_discount: null,
  is_archived: false,
  archived_reason: ""
}

let header = [
  "Паспорт",
  "ФИО",
  "Дата рождения",
  "Адрес регистрации",
  "Адрес проживания",
  "Профессия",
  "Телефоны",
  "Пол",
  "Место рождения",
  "Откуда узнали",
  "E-mail",
  "Комментарий",
  "Комментарий",
  "Баланс",
  "Скидка",
  "Архивирован",
  "Причина"
]

/**
 * Класс-компонента для отображения формы создания элементов таблицы
 */
class CreateForm extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div /*className={s.}*/>
        <table className={`${s.table} ${s.createT}`}>
          <tr>{header.map(key => <th>{key}</th>)}</tr>
          <tr id={"create"}>{header.map(key => <td contentEditable={"true"}/>)}</tr>
        </table>
        <button onClick={getFromCreateForm}><i className={"material-icons"}>send</i></button>
      </div>
    )
  }
}

function getFromCreateForm() {
  const table = document.getElementById("create");
  let tableCont = table.innerText.split("\t");
  // console.log(tableCont);
  let client = {
    id: 4,
    passport_id: tableCont[0],
    full_name: tableCont[1],
    birth_date: tableCont[2],
    address_registration: tableCont[3],
    address_residence: tableCont[4],
    occupation: tableCont[5],
    phones: tableCont[6],
    gender: tableCont[7],
    birth_place: tableCont[8],
    discovery_info: tableCont[9],
    email: tableCont[10],
    comment: tableCont[11],
    comment_addition: tableCont[12],
    balance: tableCont[13],
    permanent_discount: tableCont[14],
    is_archived: tableCont[15],
    archived_reason: tableCont[16]
  }
  document.cookie = "sessionid=50awxpj4aqzmjofu21qx9lejqb40gd5l";
  axios.post('http://localhost:8000/clients/', client, {withCredentials: true});
  // .then(Client.state.apiResponse.clients.add(client))
}

export default class Client extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showModal: false,
      apiResponse: {clients: []},
      showCreateForm: false
    };

    this.handleShow = this.handleShow.bind(this);
    this.handleHide = this.handleHide.bind(this);
    this.showCreateForm = this.showCreateForm.bind(this);
  }

  handleShow(id) {
    this.setState({showModal: true});
    this.setState({modalId: id});
  }

  handleHide() {
    this.setState({showModal: false});

  }

  showCreateForm = () => {
    this.setState({
      showCreateForm: true,
    });
  }

  callAPI() {
    axios.get('http://localhost:8000/clients', {withCredentials: true})
      .then(response => this.setState({apiResponse: response.data}));
  }

  componentWillMount() {
    document.cookie = "sessionid=50awxpj4aqzmjofu21qx9lejqb40gd5l";
    this.callAPI();
  }

  render() {
    const modal = this.state.showModal ? (
      <Modal>
        <button onClick={this.handleHide} className={"fullBtn"}/>
        <div className="modal">
          <div className="modal_text">
            <table className="table">
              <tr>{header.map(key => <th>{key}</th>)}</tr>
              {this.state.apiResponse.clients.map(client => {
                if (client.id === this.state.modalId)
                  return (
                    <tr id={client.id}>{showRow(client).map(client_el => <td>
                      <div contentEditable={"true"}>{client_el}</div>
                    </td>)}</tr>
                  )
              })}
            </table>
            <button onClick={(e) => {

            }}/>
          </div>
        </div>
      </Modal>
    ) : null;

    return (
      <BrowserRouter>
        <div className={s.div_table}>
          {/*<ReactTabulator columns={columns} data={data} options={} />*/}
          {/*{header.map(key => <div id={key} className={s.head}>{key}</div>)}*/}
          {/*<button onClick={this.handleShow}>*/}
          {/*{text.map(key => <button onClick={this.handleShow} id={key+0} className={s.text}>{key}</button>)}*/}
          {/*</button>*/}
          {modal}
          <table id="tab">
            <tr>{header.map(key => <th>{key}</th>)}</tr>
            {this.state.apiResponse.clients.map(client => <tr
              id={client.id}>{showRow(client).map(client_el => {
              // console.log(client.id)
              return (<td onClick={() => {
                this.handleShow(client.id)
              }}>{client_el}
              </td>)
            })}
              <button onClick={delElem}><i className="material-icons">delete</i></button>
            </tr>)}
          </table>
        </div>
        <button onClick={this.showCreateForm} className={s.create} id={"createEl"}><i
          className="material-icons">create</i></button>
        {this.state.showCreateForm ?
          <CreateForm/> : null}
      </BrowserRouter>
    )
  }
}

const delElem = () => {

}

let showRow = (client) => {
  let kek = [];
  for (const [key, value] of Object.entries(client)) {
    if (key !== 'id')
      kek.push(value);
  }
  return kek;
}