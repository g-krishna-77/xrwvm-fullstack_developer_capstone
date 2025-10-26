import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import positive_icon from "../assets/positive.png"
import neutral_icon from "../assets/neutral.png"
import negative_icon from "../assets/negative.png"
import review_icon from "../assets/reviewbutton.png"
import Header from '../Header/Header';

const Dealer = () => {
  const [dealer, setDealer] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [unreviewed, setUnreviewed] = useState(false);
  const [postReview, setPostReview] = useState(<></>)
  const [loading, setLoading] = useState(true);

  let curr_url = window.location.href;
  let root_url = curr_url.substring(0, curr_url.indexOf("dealer"));
  let params = useParams();
  let id = params.id;
  let dealer_url = root_url + `djangoapp/dealer/${id}`;
  let reviews_url = root_url + `djangoapp/reviews/dealer/${id}`;
  let post_review = root_url + `postreview/${id}`;
  
  // SINGLE get_dealer function (handles both array and object)
  const get_dealer = async () => {
    try {
      const res = await fetch(dealer_url, { method: "GET" });
      const retobj = await res.json();
      
      console.log("Dealer response:", retobj);
      
      if(retobj.status === 200 && retobj.dealer) {
        // Check if dealer is an object or array
        if (Array.isArray(retobj.dealer)) {
          // If it's an array, get the first element
          let dealerobjs = Array.from(retobj.dealer);
          if (dealerobjs.length > 0) {
            setDealer(dealerobjs[0]);
            console.log("Dealer set (from array):", dealerobjs[0]);
          } else {
            setDealer({});
          }
        } else {
          // If it's an object, use it directly
          setDealer(retobj.dealer);
          console.log("Dealer set (object):", retobj.dealer);
        }
      } else {
        setDealer({});
      }
    } catch (err) {
      console.error("Error fetching dealer:", err);
      setDealer({});
    }
  }

  const get_reviews = async () => {
    try {
      const res = await fetch(reviews_url, { method: "GET" });
      const retobj = await res.json();
      
      console.log("Reviews response:", retobj);
      
      if(retobj.status === 200 && retobj.reviews) {
        if(retobj.reviews.length > 0){
          setReviews(retobj.reviews);
          setUnreviewed(false);
        } else {
          setUnreviewed(true);
        }
      } else {
        setUnreviewed(true);
      }
    } catch (err) {
      console.error("Error fetching reviews:", err);
      setUnreviewed(true);
    } finally {
      setLoading(false);  // IMPORTANT: Set loading to false when done
    }
  }

  const senti_icon = (sentiment) => {
    let icon = sentiment === "positive" ? positive_icon : sentiment === "negative" ? negative_icon : neutral_icon;
    return icon;
  }

  useEffect(() => {
    get_dealer();
    get_reviews();
    
    try {
      if(typeof sessionStorage !== 'undefined' && sessionStorage.getItem("username")) {
        setPostReview(<a href={post_review}><img src={review_icon} style={{width:'10%',marginLeft:'10px',marginTop:'10px'}} alt='Post Review'/></a>)
      }
    } catch (err) {
      console.error("Session storage error:", err)
    }
  }, [id]);

  if(loading) {
    return <div style={{margin:"20px"}}><Header/><h2>Loading...</h2></div>
  }

  return(
    <div style={{margin:"20px"}}>
      <Header/>
      <div style={{marginTop:"10px"}}>
        <h1 style={{color:"grey"}}>
          {dealer && dealer.full_name ? dealer.full_name : "Dealer Not Found"}
          {postReview}
        </h1>
        {dealer && dealer.full_name && (
          <h4 style={{color:"grey"}}>
            {dealer['city']}, {dealer['address']}, Zip - {dealer['zip']}, {dealer['state']}
          </h4>
        )}
      </div>
      
      <div className="reviews_panel">
        {unreviewed === true ? <div>No reviews yet! </div> :
        reviews && reviews.length > 0 ? reviews.map((review, idx) => (
          <div key={idx} className='review_panel'>
            <img src={senti_icon(review.sentiment)} className="emotion_icon" alt='Sentiment'/>
            <div className='review'>{review.review}</div>
            <div className="reviewer">{review.name} {review.car_make} {review.car_model} {review.car_year}</div>
          </div>
        )) : <div>No reviews found</div>}
      </div>  
    </div>
  )
}

export default Dealer
