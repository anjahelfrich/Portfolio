function burgerMenu() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function homeMap() {
  var fileList = [
    "./gpxFILES/Not_clean_but_cleaner.gpx",
    "./gpxFILES/Winsor_snot_rockets_.gpx",
    "./gpxFILES/Coyote_was_sketch_.gpx",
    "./gpxFILES/Snow_drifting_on_10k.gpx",
    "./gpxFILES/North_Course_pinch_flat.gpx",
    "./gpxFILES/Jerrying_my_way_down_jagged_axe_for_the_first_time.gpx",
    "./gpxFILES/Enduro_3.gpx",
    "./gpxFILES/Angel_Fire_Day_2_bacon_strips_.gpx",
    "./gpxFILES/Sam_protecting_his_good_side_.gpx",
    "./gpxFILES/Dirt_Fiesta_lap_2.gpx",
    "./gpxFILES/Copper_Chill.gpx",
    "./gpxFILES/Trying_to_keep_up_with_Sarah_and_Jessie.gpx",
    "./gpxFILES/Pine_flats_w_Corinna.gpx",
    "./gpxFILES/Lackadaisical.gpx",
    "./gpxFILES/Monster_Loop_Variation_w_Sam.gpx",
    "./gpxFILES/Trying_to_get_my_childhood_friend_Georgia_into_MTB.gpx",
    "./gpxFILES/Kind_of_a_spastic_I_suck_sort_of_ride_.gpx",
    "./gpxFILES/Angel_Fire_Day_1.gpx",
    "./gpxFILES/Evening_Mountain_Bike_Ride.gpx",
    "./gpxFILES/Lunch_Mountain_Bike_Ride.gpx",
    "./gpxFILES/Top_to_bottom_with_Sam_and_his_Dad_.gpx",
    "./gpxFILES/High_Desert_ride_lower_sandias.gpx",
    "./gpxFILES/Power_line_sans_rain_is_there_a_more_fun_way_to_get_there_.gpx",
    "./gpxFILES/Reward_for_doing_job_applications_all_day.gpx",
    "./gpxFILES/Fall_hikers_out_in_full_force.gpx",
    "./gpxFILES/Working_on_Endurance.gpx",
    "./gpxFILES/Georgia_placitas_ride.gpx",
    "./gpxFILES/Evening_Ride.gpx",
    "./gpxFILES/Cedro_SamJosh.gpx",
    "./gpxFILES/Gutierrez_Ride_with_Corinna.gpx",
    "./gpxFILES/Running_out_of_daylight_and_front_brakes.gpx",
    "./gpxFILES/Tinker_Town_Twofer.gpx",
  ]

  var map = L.map('map').setView([35.675517, -105.945269],8)

  L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}.', {
    attribution: 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC'
  }).addTo(map);

  var customLayer = L.geoJson(null, {
  style: function(feature) {
    return { color: '#CA6702', weight: 2 };
  },
  onEachFeature: function(feature, layer) {
    if (feature.properties.name) {
      layer.bindPopup(feature.properties.name);
    }
  }
});

  for (var i = 0; i < fileList.length; i += 1) {
  omnivore.gpx(fileList[i], null, customLayer).addTo(map);
  }
}
