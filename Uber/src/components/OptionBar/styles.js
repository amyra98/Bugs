import {StyleSheet} from 'react-native';

const styles = StyleSheet.create({

    containerBox:{
        padding : 5,
    },

    header:{
        padding : 10,
        margin : 5,
        fontSize : 25,
        fontWeight : 'bold',
    },

    busInfo:{
        margin:10,
        padding : 3,
        shadowColor: "black",
        shadowOffset: {height: 2},
        shadowOpacity: 0.3,
    }, 

    busText :{
        fontSize : 15,
    },

    button:{
        width : 300,
        alignSelf : 'center',
        margin:5,
        padding : 5,
        shadowColor: "black",
        shadowOffset: {height: 2},
        shadowOpacity: 0.3,
        flexDirection : 'row',
        alignItems:'center',
        borderColor:'black',
        borderWidth : 1,
        borderRadius : 10
    }, 

    buttonText:{
        fontSize : 20
    }

});

export default styles;
