# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_22:29:30_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-05-15 22:29:30 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-15 22:29:30 UTC

- **83,857** saved flights
- **30,288** unique routes
- **129** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **83,857** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,031,750.4 tonnes** estimated CO2 emissions
- **59,811,619 km** total distance flown
- **865 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3592 |
| 2 | SkyWest Airlines | 3114 |
| 3 | IndiGo | 1809 |
| 4 | EJA | 1581 |
| 5 | American Airlines | 1291 |
| 6 | Southwest Airlines | 1229 |
| 7 | Lufthansa | 1069 |
| 8 | ENY | 1047 |
| 9 | Delta Air Lines | 917 |
| 10 | Vueling | 794 |
| 11 | LATAM Airlines | 757 |
| 12 | AXM | 751 |
| 13 | WIF | 726 |
| 14 | AZU | 659 |
| 15 | All Nippon Airways | 652 |
| 16 | Swiss International | 648 |
| 17 | LXJ | 616 |
| 18 | QLK | 615 |
| 19 | Alaska Airlines | 592 |
| 20 | easyJet | 551 |
| 21 | EJU | 534 |
| 22 | AEE | 529 |
| 23 | Cathay Pacific | 522 |
| 24 | VIV | 502 |
| 25 | Air France | 490 |
| 26 | Japan Airlines | 468 |
| 27 | CXK | 445 |
| 28 | AXB | 444 |
| 29 | MXY | 420 |
| 30 | United Airlines | 413 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 68814 |
| 2 | 🇪🇸 ES | 5932 |
| 3 | 🇮🇳 IN | 5658 |
| 4 | 🇦🇺 AU | 5330 |
| 5 | 🇩🇪 DE | 4666 |
| 6 | 🇮🇹 IT | 4632 |
| 7 | 🇧🇷 BR | 4619 |
| 8 | 🇯🇵 JP | 4195 |
| 9 | 🇨🇦 CA | 4181 |
| 10 | 🇬🇧 GB | 3570 |
| 11 | 🇫🇷 FR | 3322 |
| 12 | 🇨🇴 CO | 2809 |
| 13 | 🇲🇽 MX | 2549 |
| 14 | 🇬🇷 GR | 2429 |
| 15 | 🇳🇴 NO | 2334 |
| 16 | 🇨🇭 CH | 2218 |
| 17 | 🇲🇾 MY | 1890 |
| 18 | 🇿🇦 ZA | 1574 |
| 19 | 🇹🇷 TR | 1488 |
| 20 | 🇳🇿 NZ | 1469 |
| 21 | 🇹🇭 TH | 1453 |
| 22 | 🇵🇱 PL | 1393 |
| 23 | 🇵🇭 PH | 1310 |
| 24 | 🇬🇹 GT | 1272 |
| 25 | 🇰🇷 KR | 1272 |
| 26 | 🇲🇦 MA | 975 |
| 27 | 🇲🇴 MO | 960 |
| 28 | 🇲🇪 ME | 886 |
| 29 | 🇳🇱 NL | 860 |
| 30 | 🇭🇷 HR | 752 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1840 |
| 2 | Denver International Airport |  | US | 1413 |
| 3 | Tokyo International Airport |  | JP | 1406 |
| 4 | Indira Gandhi International Airport |  | IN | 1202 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1179 |
| 6 | Frankfurt am Main International Airport |  | DE | 1081 |
| 7 | Harry Reid International Airport |  | US | 1046 |
| 8 | Zurich Airport |  | CH | 994 |
| 9 | La Aurora Airport |  | GT | 965 |
| 10 | Macau International Airport |  | MO | 960 |
| 11 | Guaymaral Airport |  | CO | 948 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 934 |
| 13 | El Dorado International Airport |  | CO | 903 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 842 |
| 15 | Chicago O'Hare International Airport |  | US | 813 |
| 16 | Madrid Barajas International Airport |  | ES | 763 |
| 17 | Kuala Lumpur International Airport |  | MY | 751 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 726 |
| 19 | Salt Lake City International Airport |  | US | 700 |
| 20 | Malpensa International Airport |  | IT | 700 |
| 21 | Sydney Kingsford Smith International Airport |  | AU | 699 |
| 22 | Bengaluru International Airport |  | IN | 695 |
| 23 | Capua Airport |  | IT | 683 |
| 24 | Charles de Gaulle International Airport |  | FR | 654 |
| 25 | Charlotte/Douglas International Airport |  | US | 652 |
| 26 | Congonhas Airport |  | BR | 652 |
| 27 | Tenerife Norte Airport |  | ES | 606 |
| 28 | Daniel K Inouye International Airport |  | US | 605 |
| 29 | Ninoy Aquino International Airport |  | PH | 599 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 589 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 566 |
| 32 | Barcelona International Airport |  | ES | 561 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 559 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 540 |
| 35 | Vitoria/Foronda Airport |  | ES | 531 |
| 36 | Don Mueang International Airport |  | TH | 523 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 523 |
| 38 | Amsterdam Airport Schiphol |  | NL | 521 |
| 39 | O. R. Tambo International Airport |  | ZA | 494 |
| 40 | Calgary International Airport |  | CA | 492 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 393 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 303 | 21m | 244 km | 1,275.8 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 273 | 1h 8m | 706 km | 3,323.8 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 237 | 24m | 225 km | 919.4 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 222 | 28m | 304 km | 1,163.8 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 221 | 1h 26m | 910 km | 3,468.0 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 215 | 14m | 114 km | 421.7 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 215 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 197 | 31m | - | - |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 189 | 19m | 165 km | 537.6 t |
| 11 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 188 | 1h 11m | 770 km | 2,497.4 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 175 | 26m | 275 km | 829.3 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 143 | 20m | 99 km | 244.9 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 139 | 44m | 452 km | 1,083.3 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 129 | 31m | 369 km | 821.1 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 126 | 27m | 152 km | 329.3 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 125 | 27m | 215 km | 462.9 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 123 | 20m | 147 km | 311.3 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 119 | 14m | 154 km | 315.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 119 | 23m | 55 km | 113.1 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 118 | 20m | 250 km | 509.7 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 110 | 57m | 493 km | 935.8 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 107 | 1h 43m | 1,423 km | 2,625.9 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 107 | 13m | - | - |
| 27 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 28 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 106 | 18m | 144 km | 263.7 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 101 | 1h 18m | 961 km | 1,674.1 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| CGDKX | CGD | Ottawa / Rockcliffe Airport (CYRO) | Ottawa / Rockcliffe Airport (CYRO) | 2026-05-15 22:10 UTC | 2026-05-15 22:29 UTC | 19m |
| N324AJ |  | Auburn Municipal Airport (KAUN) | San Carlos Airport (KSQL) | 2026-05-15 21:46 UTC | 2026-05-15 22:25 UTC | 39m |
| CPA382 | Cathay Pacific | Zurich Airport (LSZH) | Macau International Airport (VMMC) | 2026-05-15 11:50 UTC | 2026-05-15 22:22 UTC | 10h 32m |
| CXK168 | CXK | Ogden-Hinckley Airport (KOGD) | Nephi Municipal Airport (KU14) | 2026-05-15 21:30 UTC | 2026-05-15 22:22 UTC | 52m |
| N73047 |  | Merrill Field (PAMR) | Beluga Airport (PABG) | 2026-05-15 21:56 UTC | 2026-05-15 22:19 UTC | 23m |
| N6847U |  | Lincoln Regional/Karl Harder Field (KLHM) | Willows/Glenn County Airport (KWLW) | 2026-05-15 21:20 UTC | 2026-05-15 22:17 UTC | 56m |
| N881PM |  | Palo Alto Airport (KPAO) | Tracy Municipal Airport (KTCY) | 2026-05-15 21:55 UTC | 2026-05-15 22:15 UTC | 19m |
| COBRA05 | COB | Edwards Af Aux North Base Airport (K9L2) | Boron Airstrip (57CL) | 2026-05-15 21:45 UTC | 2026-05-15 22:07 UTC | 21m |
| N64012 |  | Merrill Field (PAMR) | Wasilla Airport (PAWS) | 2026-05-15 21:32 UTC | 2026-05-15 22:05 UTC | 33m |
| N4313D |  | 16PA (16PA) | Rostraver Airport (KFWQ) | 2026-05-15 21:24 UTC | 2026-05-15 22:03 UTC | 39m |
| N365TG |  | Harford County Airport (K0W3) | Ocean City Municipal Airport (KOXB) | 2026-05-15 21:29 UTC | 2026-05-15 22:02 UTC | 32m |
| N805DZ |  | Yolo County Airport (KDWA) | Yolo County Airport (KDWA) | 2026-05-15 21:46 UTC | 2026-05-15 22:01 UTC | 14m |
| N5266D |  | Bolingbrook's Clow International Airport (K1C5) | Morris Municipal/James R Washburn Field (KC09) | 2026-05-15 21:35 UTC | 2026-05-15 21:59 UTC | 24m |
| N810EB |  | Gunnersfield Ranch Airport (71CL) | Gunnersfield Ranch Airport (71CL) | 2026-05-15 20:43 UTC | 2026-05-15 21:59 UTC | 1h 16m |
| N100BW |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-05-15 21:38 UTC | 2026-05-15 21:58 UTC | 19m |
| N2YV |  | Talkeetna Airport (PATK) | Nugget Bench Airport (33AK) | 2026-05-15 21:36 UTC | 2026-05-15 21:56 UTC | 20m |
| CPA270 | Cathay Pacific | Amsterdam Airport Schiphol (EHAM) | Zhuhai Airport (ZGSD) | 2026-05-15 10:55 UTC | 2026-05-15 21:54 UTC | 10h 59m |
| THY6830 | Turkish Airlines | Hamburg-Finkenwerder Airport (EDHI) | Istanbul Hezarfen Airfield (LTBW) | 2026-05-15 19:30 UTC | 2026-05-15 21:53 UTC | 2h 23m |
| CXK508 | CXK | Denton Enterprise Airport (KDTO) | Addington Field (4TX8) | 2026-05-15 21:38 UTC | 2026-05-15 21:49 UTC | 11m |
| N425KS |  | Charleston Afb/International Airport (KCHS) | Johnson County Airport (K6A4) | 2026-05-15 20:47 UTC | 2026-05-15 21:48 UTC | 1h 1m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
