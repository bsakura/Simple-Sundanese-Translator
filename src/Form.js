import React from 'react'
import './Form.css'
import ReactDOM from 'react-dom'
const path = require('path')


export default class MainForm extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            key : "",
            algorithm: 0,
            bhs: 0,
            hasils : ""
        }
        
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.onChooseM = this.onChooseM.bind(this);
        this.onChooseL = this.onChooseL.bind(this);
    }
    
    onChooseL(id) {
        this.setState({
            bhs: id
        })
    }

    onChooseM(id) {
        this.setState({
            algorithm: id
        })
    }

    handleChange(event){
        // console.log(event.target.name)
        const {name, value, type, checked} = event.target
        this.setState({[event.target.name] : value})   
    }

    handleSubmit(){
        console.log(this.state)
        this.setState({hasils : ""})
        fetch("http://localhost:5000/query",{
            method : 'post',
            headers : {'Content-type' : 'application/json'},
            body : JSON.stringify({
                'key' : this.state.key,
                'algorithm' : this.state.algorithm,
                'bhs' : this.state.bhs
            })
        }).then(e => e.json())
            .then(data => this.setState({hasils : data.data}))
    }

    

    render(){
        const { active, value, error, label } = this.state;
        const { predicted, locked } = this.props;
        const fieldClassName = `field ${(locked ? active : active || value) &&
        "active"} ${locked && !active && "locked"}`;

        return (
            <div>
                <div className="split left">
                <div className="Formulir">
                    <div>
                    <div className="FormLabel">
                        Algoritma:
                    </div>
                    <div>
                        <label class="container">
                            Knuth Morris Pratt
                            <input type="radio" name="algorithm" onChange={() => this.onChooseM(0)} checked={this.state.algorithm == 0} />
                            <span class="checkmark"></span>
                        </label>
                    </div>
                    <div>
                        <label class="container">
                            Booyer Moore
                            <input type="radio" name="algorithm" onChange={() => this.onChooseM(1)} checked={this.state.algorithm == 1} />
                            <span class="checkmark"></span>
                        </label>
                    </div>
                    <div>
                        <label class="container">
                            Regex
                            <input type="radio" name="algorithm" onChange={() => this.onChooseM(2)} checked={this.state.algorithm == 2} />
                            <span class="checkmark"></span>
                        </label>
                    </div>
                    <br />
                    </div>
                    <div className="FormLabel">
                        Bahasa:
                    </div>
                    <div>
                        <label class="container">Indonesia-Sunda
                            <input type="radio" name="bhs" onChange={() => this.onChooseL(0)} checked={this.state.bhs == 0} />
                            <span class="checkmark"></span>
                        </label>
                    </div>
                    <div>
                        <label class="container">Sunda-Indonesia
                            <input type="radio" name="bhs" onChange={() => this.onChooseL(1)} checked={this.state.bhs == 1} />
                            <span class="checkmark"></span>
                        </label>
                    </div>
                    </div>
                    <br />

                    <div className="split right">
                       <div className={fieldClassName}>
                            {active &&
                                value &&
                                predicted &&
                                predicted.includes(value) && 
                                <p className="predicted">
                                    {predicted}
                                </p>
                            }
                            <input
                                id={1}
                                type="text"
                                name="key"
                                value={value}
                                placeholder={"Apeni"}
                                onChange={this.handleChange}
                                onFocus={() => !locked && this.setState({ active: true })}
                                onBlur={() => !locked && this.setState({ active: false })}
                            />
                            <label htmlFor={1} className={error && "error"}>
                                {error || label}
                            </label>
                        </div>
                        
                    <div>
                        <button onClick={this.handleSubmit} name="submit" className="button">Translate</button>
                    </div>
                    <div className="outp">
                        <p>{this.state.hasils || ""}</p>
                    </div>
                    </div>
                    
                </div>
            </div>
        )
    }
}