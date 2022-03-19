import React from "react";
import {View, Text} from "react-native";

import Avatar, { IconTypes, Sizes } from 'rn-avatar';
import styles from './styles.js';

const OptionBar = (props) => {
    return (
        <View style={styles.containerBox}>

            <Text style={styles.header}>
                Regarding your upcoming trip
            </Text>

            <View style={styles.busInfo}>
                <Text style = {styles.busText}> ETA : 12 min</Text>
            </View>
            
            <View style = {styles.button}>
                <Avatar
                rounded
                size={Sizes.MEDIUM}
                source={require('../../assets/avatars/b.png')}
                title='John Doe2'
                containerStyle={{ margin: 10 }}
                />
                <Text style={styles.buttonText}> Cancel My Ride </Text>
            </View>

            
            <View style = {styles.button}>
                <Avatar
                rounded
                size={Sizes.MEDIUM}
                source={require('../../assets/avatars/c.png')}
                title='John Doe3'
                containerStyle={{ margin: 10 }}
                />
                <Text style={styles.buttonText}> I'm running late </Text>
            </View>
       

        </View>
    );
};

export default OptionBar;
