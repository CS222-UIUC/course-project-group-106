import './Home.css'
import SpendingPieChart from '../assets/Spending Pie Chart.png';
import SpendingOverTime from '../assets/Spending Over Time.png';

function Home() {
    return (
        <div className='home_content'>
            <h1 className='home_h1'>Home</h1>
            <p className='home_p'>This app will help track your budget -- how much you spend and on what. To use our app, head to the projects tab!</p>
            <div className='home_image-with-text'>
                <img className = 'home_image-with-text_centered' src={SpendingPieChart} alt="Spending Pie Chart"></img>
                <p className='home_image-with-text_centered'>Spending/Category Example Pie Chart</p>
            </div>
            <div className='home_image-with-text'>
                <img className = 'home_image-with-text_centered' src={SpendingOverTime} alt="Spending Over Time"></img>
                <p className='home_image-with-text_centered'>Spending/Time Example Graph</p>
            </div>
        </div>
    );
}

export {Home};