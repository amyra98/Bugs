 import React from "react";
 import {View, Text} from "react-native";

 import TopBar from "../../components/TopBar";
 import Map from "../../components/Map";
 import OptionBar from "../../components/OptionBar"

 const HomeScreen = (props) => {
     return (
         <View>
            <TopBar />
            <Map />
            <OptionBar />
         </View>
     );
 };

 export default HomeScreen;