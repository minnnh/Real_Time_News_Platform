import './NewsCard.css';
import React from 'react';
import Auth from '../Auth/Auth';

const WEB_SERVER = 'http://localhost:3000'

class NewsCard extends React.Component {
    redirectToUrl(url, event) {
        event.preventDefault();
        this.sendClickLog();
        window.open(url, '_blank');
    }

    sendClickLog() {
        const url = WEB_SERVER +
            '/news/userId/' + Auth.getEmail() + '/newsId/' + this.props.news.digest;
    
        const request = new Request(
          encodeURI(url),
          {
            method: 'POST',
            headers: { 'Authorization': 'bearer ' + Auth.getToken()},
          });
    
        fetch(request);
    }

    render() {
      if (this.props.news.urlToImage == null || this.props.news.urlToImage == '') return
      // const isoDateString = this.props.publishedAt;

      // // Extract the date part
      // const matchResult = isoDateString && isoDateString.match(/\("(.+)"\)/);
      // // Convert the extracted date string to a Date object
      // const extractedDate = new Date(extractedDateString);

      // // Use extractedDate to format the date as a string
      // const formattedDate = extractedDate.toLocaleDateString('en-US');

        return(
         <div className="news-container" onClick={(event) => this.redirectToUrl(this.props.news.url, event)}>
           <div className='row'>
               <div className='col s4 fill'>
               <img src={this.props.news.urlToImage} alt='news'/>
               </div>
               <div className="col s8">
                  <div className="news-intro-col">
                    <div className="news-intro-panel">
                     <h4>{this.props.news.title}</h4>
                     <div className="news-description">
                     <p>{this.props.news.description}</p>
                       <div>
                          {this.props.news.source != null && <div className='chip light-blue news-chip'>{this.props.news.source}</div>}
                          {this.props.news.reason != null && <div className='chip light-green news-chip'>{this.props.news.reason}</div>}
                          {this.props.news.published_date != null && <div className='chip amber news-chip'>{this.props.news.published_date}</div>}
                       </div>
                     </div>
                    </div>
                  </div>
               </div>
           </div>
         </div>
        );

    }
}

export default NewsCard;