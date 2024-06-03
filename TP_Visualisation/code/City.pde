class City { 
      int postalcode; 
      String name; 
      float x; 
      float y; 
      float population; 
      float density;
      float radius;
      boolean hovered;
      boolean selected;

      public City(int postalCode,String Name,float X,float Y,float Population,float Density){
        postalcode = postalCode;
        name = Name;
        x = X;
        y = Y;
        population = Population;
        density = Density;
        hovered = false;
        selected = false;
      }
      
      void draw(){
        //set((int) mapX(this.x), (int) mapY(this.y), color(0));
        
        // densité avec couleur
        // population avec taille
        float seuil = seuilDensite(this.density);
        radius = seuilPopulation(this.population);
        float textMargin = 10;
        
        strokeWeight(1);
        
        if (hovered){
          textSize(15);
          fill(255);
          
          rect((int) mapX(this.x)+radius-(textMargin/2), (int) mapY(this.y)-12, textWidth(name)+textMargin,15);
          strokeWeight(3);
          fill(0);
          
          //textAlign(LEFT);
          if (selected){
             fill(0,150,0);
          }
          text(name, mapX(x)+radius,mapY(y));
        }      
        fill(255,seuil,seuil);
        if (selected){
          fill(seuil,255,seuil);
        } 
        circle((int) mapX(this.x), (int) mapY(this.y),radius);
       
        
      }
      
      boolean contains(int px, int py){
        return dist(mapX(x), mapY(y), px, py) <= radius;
        
      }
}
