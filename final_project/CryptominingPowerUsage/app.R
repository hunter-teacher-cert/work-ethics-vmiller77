#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(dplyr)

# reading in mining file
minerData <- read.csv(file = 'miners.csv')
minerNames <- minerData$miner

# reading in appliance file
appliancesData <- read.csv(file = 'appliances.csv')
applianceNames <- appliancesData$appliance
applianceWatts <- appliancesData$watts_per_hour

# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("How much power do crypto-miners use?"),

    # Select the miner
    selectInput("miner", label = h3("Select miner"), 
                choices = minerNames, 
                selected = 1),
    
    # Select the appliance
    selectInput("appliance", label = h3("Select appliance"), 
                choices = applianceNames, 
                selected = 1),
    
    #Text Output
    textOutput("result1"),
    textOutput("result2"),
    textOutput("conversion"),
    tags$head(tags$style("#conversion{color: red;
                                 font-size: 20px;
                                 font-style: italic;
                                 }"
    )
    )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    output$result1 <- renderText({
        paste("You chose", input$miner)
        
    })
    
    output$result2 <- renderText({
        paste("You chose the appliance", input$appliance)
        
    })
    
    output$conversion <- renderText({
        conversionRate <- conversion(input$miner, input$appliance)
        
        paste("You could have powered", conversionRate, input$appliance,
              "instead of a", input$miner, "for 1 hour.")
        
    })
    
}

#conversion function
conversion <- function(minerName, applianceName){
    #finding the wattage per hour for miner and appliance
    minerWatts <- minerData %>% filter(miner == minerName)
    minerWatts <- minerWatts$watts
    applianceWatts <- appliancesData %>% filter(appliance == applianceName)
    applianceWatts <- applianceWatts$watts
    
    #get conversion and format to 2 decimal places
    conversionRate <- format((minerWatts/applianceWatts), nsmall = 3)
    
    #return the conversion rate
    return(conversionRate)
    
}

# Run the application 
shinyApp(ui = ui, server = server)
