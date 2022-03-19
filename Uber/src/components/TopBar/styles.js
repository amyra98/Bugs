import {StyleSheet} from 'react-native';



const styles = StyleSheet.create({

    topBox:{
        height : 60,
        justifyContent : 'space-between',
        alignItems : 'center', 
        padding : 10,
        flexDirection:'row',
        margin:10
    },

    menuIcon:{
        shadowColor: "black",
        shadowOffset: {height: 2},
        shadowOpacity: 0.3,
    }
});

export default styles;