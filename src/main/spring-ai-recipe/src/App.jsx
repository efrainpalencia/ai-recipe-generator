import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import './App.css'
import RecipeGenerator from './components/RecipeGenerator/RecipeGenerator'

function App() {

  return (
    <>
      <Container>
        <Row>
          <Col>
          <RecipeGenerator />
          </Col>
        </Row>
      </Container>
    </>
  )
}

export default App
