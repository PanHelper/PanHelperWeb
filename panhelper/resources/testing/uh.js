import React from "react";
import Footer from "../components/footer";
import SideBar from "../components/sideBar";

import Hero from "../components/homepage/HeroSection.jsx";
import Mission from "../components/homepage/MissionStatement.jsx";
import SellingPointL from "../components/homepage/SellingPointL.jsx";
import SellingPointR from "../components/homepage/SellingPointR.jsx";
import FinalSell from "../components/homepage/Final.jsx";
import "./homePage.css";

import BMFA from "../images/homeImages/bostonMFA.jpg";
import AMNH from "../images/homeImages/newyorkNatHist.jpg";
import MOMA from "../images/homeImages/MOMA.jpg";

function homePage() {
  return (
    <div
      className="App"
      style={{ backgroundColor: "#E2D6C0", width: "100%", height: "100%" }}
    >
      <div
        style={{ width: "100%", height: "30px", backgroundColor: "#FDF3DE" }}
      ></div>
      <div style={{ backgroundColor: "#FDF3DE" }}>
        <div
          style={{
            display: "flex",
            justifyContent: "left",
            //alignItems: "flex-start",
            // height: "82vh",
            borderRadius: "20px",
            background: "#E2D6C0",
            marginRight: "40px",
            marginLeft: "170px",
            paddingTop: "20px",
          }}
        >
          <main>
            <Hero />
            <Mission />
            <SellingPointL
              museumImg={BMFA}
              imgWidth={250}
              museumName="Boston Museum of Fine Arts"
              sellingTitle="Unique, Illustrated Stamps for every Museum"
              sellingText1="For every museum you visit you collect a stamp unique to that museum. And the more you go, the higher the chance of getting special achievement stamps for supporting your local museums!"
              sellingText2="In addition to the stamps, you also collect unique stickers depending on what type of museum you visit! For instance, if you vistit the Intrepid in New York City, you collect its unique sticker."
            />

            <SellingPointR
              museumImg={AMNH}
              imgWidth={350}
              museumName="American Museum of Natural History"
              sellingTitle="Key Into Limited-Time Exhibits"
              sellingText1="We also offer stamps for limited run exhibits so you can remember your special times there and have something commemorative that you don’t have to spend exuberant amounts of money on like most museum gift shop plushies and t-shirts."
              sellingText2="All of our stamps are unique to museums, thus it follows that limited run exhibits will also be unique and unavailable after the museum itself closes the exhibit's doors. Tickets are a fickle thing, they can get lost in the washing machine, get wet and disintegrate, or fall out on a train or bus, never to be seen again, but Museo keeps all of your normal exhibit tickets and limited run exhibits so you never have to worry about forgetting an experience because you lost a piece of paper."
            />

            <SellingPointL
              museumImg={MOMA}
              imgWidth={300}
              museumName="NYC Museum of Modern Art"
              sellingTitle="Social Media Without The Brainrot!"
              sellingText1="Museo is a social form of media that is not social media! Museo gives you the option to friend people you know to see what places they’ve been and what exhibits they like. It makes it easier to trade stories, give recommendations, and plan trips to visit more museums and collect more stamps."
              sellingText2="We are a social media that encourages getting offline. As you collect more stamps and stickers, you visit more museums, and in turn get to show your friends the places you've been. Our memory book is designed to be shown and passed around, an achievement to be proud of. We make sure that you have a platform to collect and share all of those museum experiences that you can unplug for and hold dear."
            />

            <FinalSell />
          </main>
        </div>
      </div>
      <div style={{ position: "fixed", top: 0, left: 0 }}>
        <SideBar />
      </div>
      <Footer />
    </div>
  );
}
export default homePage;