import React from "react";
import {View, Text} from "react-native";

import Avatar, { IconTypes, Sizes } from 'rn-avatar';
import Feather from 'react-native-vector-icons/Feather';
import styles from './styles.js';

const TopBar = (props) => {
    return (
        <View style={styles.topBox}>

            <Feather 
            name={'menu'} 
            style={styles.menuIcon} 
            size = {30} />
            
            <Avatar
            rounded
            size={Sizes.MEDIUM}
            source={require('../../assets/avatars/a.png')}
            title='John Doe'
            containerStyle={{ margin: 10 }}
            />

        </View>
    );
};

export default TopBar;
