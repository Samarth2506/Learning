generate_new_data <-
  function(Airline, Month,Model,Day) {
    
    new_flight_tbl <- tibble(
      Airline  = Airline,
      Month = Month,
      Day = Day,
      Model = Model
    )
  }

Mode <- function(x) {
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}

make_preds <- function(train_data,ml_model,Airline,Month,Day,choice){
  data = train_data[train_data$AIRLINE == Airline, ]
  data = data[data$MONTH == Month,]
  data = data[data$DAY == Day,]
  
  if (dim(data)[1] == 0){
    return("There are no flights scheduled for this date and airline. Please try a different input!")
  }
  
  if(choice == 1){
    pred_probs = predict(ml_model,data, type = "response")
    preds = ifelse(pred_probs>0.35, "1","0")
  }
  
  else{
    preds = predict(ml_model,data, type = "class")
  }
  
  conf_matrix <- table(data$delayed, preds)
  accuracy <- sum(diag(conf_matrix))/sum(conf_matrix)
  if (is.na(accuracy)){
    return("There are no flights scheduled for this date and airline. Please try a different input!")
  }
  output_string = paste("The predicted value is", Mode(preds),
                        "and the accuracy of the prediction is",
                        accuracy*100)
  return(output_string)
}
