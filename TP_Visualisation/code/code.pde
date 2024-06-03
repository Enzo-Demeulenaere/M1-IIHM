float minX, maxX;
float minY, maxY;
int totalCount; // total number of places
int minPopulation, maxPopulation;
int minSurface, maxSurface;
int minAltitude, maxAltitude;
float minDensite,maxDensite;
float minPopulationToDisplay;
City lastCity = null;
//int x = 1;
//int y = 2;
//float xList[];
//float yList[];
City cities[];
float sliderPositionX = 50;
float sliderPositionY = 740;
float sliderWidth = 500;
float sliderHeight = 20;
boolean dragging = false;
float handlePosition = 50;


void setup() {
  size(900,800);
  readData();
  minPopulationToDisplay = 0;
}

void draw(){
  background(255);
  
  handlePosition = map(minPopulationToDisplay,minPopulation,maxPopulation,sliderPositionX,sliderPositionX+sliderWidth);
  for (int i = 0 ; i < totalCount-2 ; i++)
      if (cities[i].population > minPopulationToDisplay){
        cities[i].draw();
      }
  fill(0);
  textSize(24);
  String s = "Afficher les populations supérieures à " + str(minPopulationToDisplay);
  text(s,50,730);
  drawSlider();
}

void drawSlider(){
  float x = sliderPositionX;
  float y = sliderPositionY;
  float w = sliderWidth;
  float h = sliderHeight;
  String textMin = str(minPopulation);
  String textMax = str(maxPopulation);
  fill(200);
  rect(x,y, w, h);
  fill(150);
  rect(handlePosition,y,5,h);
  fill(0);
  textSize(12);
  text(textMin, x, y + h +20);
  text(textMax, x+w, y+h +20);
  
}

void readData(){
  String[] lines = loadStrings("../villes.tsv");
  parseInfo(lines[0]);
  cities = new City[totalCount];
  //xList = new float[totalCount];
  //yList = new float[totalCount];
  for (int i = 2 ; i < totalCount ; ++i) {
    String[] columns = split(lines[i], TAB);
    int postalCode = int (columns[0]);
    String name = columns[4];
    float x = float (columns[1]);
    float y = float (columns[2]);
    float population = float(columns[5]);
    float density = population / float(columns[6]);
    cities[i-2] = new City(postalCode,name,x,y,population,density);  
  }
}

void parseInfo(String line) {
  String infoString = line.substring(2); // remove the #
  String[] infoPieces = split(infoString, ',');
  totalCount = int(infoPieces[0]);
  minX = float(infoPieces[1]);
  maxX = float(infoPieces[2]);
  minY = float(infoPieces[3]);
  maxY = float(infoPieces[4]);
  minPopulation = int(infoPieces[5]);
  maxPopulation = int(infoPieces[6]);
  minSurface = int(infoPieces[7]);
  maxSurface = int(infoPieces[8]);
  minAltitude = int(infoPieces[9]);
  maxAltitude = int(infoPieces[10]);
}

void keyPressed(){
  if (key == CODED){
    if (keyCode == LEFT){
      minPopulationToDisplay /= 2;
    }
    if (keyCode == RIGHT){
      minPopulationToDisplay *= 2;
    }
  }
  redraw();
}

void mouseMoved(){
  //println(mouseX,mouseY);
  //for (int i = 0; i <= cities.length-1;i++){
  //  cities[i].selected = false;
  //}
  code.City city = pick(mouseX,mouseY);
  if ((city != null) && (city != lastCity)){
    city.hovered = true;
    println(city.name);
    if (lastCity != null){
      lastCity.hovered = false;
    }
    lastCity = city;
    
  }
  redraw();
}

void mouseClicked(){
  code.City city = pick(mouseX,mouseY);
  if ((city != null)){
    city.selected = ! city.selected;
  }
  redraw();
}

void mousePressed(){
  float dist = dist(mouseX,mouseY,handlePosition,sliderPositionY +sliderHeight);
  
  if(dist <20){
    dragging = true;
  }
}

void mouseDragged(){
  if (dragging){
    float newPos = constrain(mouseX, sliderPositionX,sliderPositionX+sliderWidth);
    handlePosition = newPos;
    minPopulationToDisplay = int(map(handlePosition, sliderPositionX, sliderPositionX + sliderWidth, minPopulation, maxPopulation));
    readData();
    redraw();    
  }
}

void mouseReleased(){
  dragging = false;
  redraw();
}

City pick(int px, int py){
  City res = null;
  for (int i = 0; i <= cities.length -1; i++){
    City city = cities[i];
    if (city != null){
      if (city.contains(px,py)){
      res = city;
      }
    }
    
  }
  return res;
}


float mapX(float x) {
 return map(x, minX, maxX, 0, 800);
}

float mapY(float y) {
 return map(y, minY, maxY, 800, 0);
}

float seuilPopulation(float pop){
  if (pop < 10000) return 1;
  if (pop < 50000) return 8;
  if (pop < 100000) return 15;
  if (pop < 500000) return 20;
  return 50;
}

float seuilDensite(float densite){
  if (densite < 0) return 250;
  if (densite < 100) return 175;
  if (densite < 1000) return 100;
  return 180;
}
