import React from 'react'


class TODOForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {text: '', author: props.author[0].uuid, project: props.project[0].uuid }
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createTODO(this.state.text, this.state.author, this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>

                <div className="form-group">
                    <label htmlFor="author">author</label>
                    <select name="author" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.author.map((item) => <option value={item.uuid}>{item.first_name}</option>)}
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="project">project</label>
                    <select name="project" className='form-control' onChange={(event) => this.handleChange(event)}>
                        {this.props.project.map((item) => <option value={item.uuid}>{item.name}</option>)}
                    </select>
                </div>

                <div className="form-group">
                    <label for="text">text</label>
                    <input type="text" className="form-control" name="text" value={this.state.text}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default TODOForm