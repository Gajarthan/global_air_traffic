# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_14:00:37_UTC-green)

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

**Latest saved flight:** 2026-05-19 14:00:37 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-19 14:00:37 UTC

- **87,976** saved flights
- **31,439** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **87,976** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,089,511.1 tonnes** estimated CO2 emissions
- **63,160,062 km** total distance flown
- **870 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3771 |
| 2 | SkyWest Airlines | 3259 |
| 3 | IndiGo | 1873 |
| 4 | EJA | 1667 |
| 5 | American Airlines | 1351 |
| 6 | Southwest Airlines | 1280 |
| 7 | Lufthansa | 1107 |
| 8 | ENY | 1091 |
| 9 | Delta Air Lines | 965 |
| 10 | Vueling | 841 |
| 11 | LATAM Airlines | 792 |
| 12 | AXM | 786 |
| 13 | WIF | 758 |
| 14 | AZU | 699 |
| 15 | Swiss International | 680 |
| 16 | All Nippon Airways | 669 |
| 17 | LXJ | 646 |
| 18 | QLK | 626 |
| 19 | Alaska Airlines | 624 |
| 20 | easyJet | 580 |
| 21 | EJU | 566 |
| 22 | Cathay Pacific | 562 |
| 23 | AEE | 547 |
| 24 | VIV | 528 |
| 25 | Air France | 516 |
| 26 | Japan Airlines | 479 |
| 27 | CXK | 464 |
| 28 | AXB | 458 |
| 29 | MXY | 450 |
| 30 | AIQ | 431 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 72156 |
| 2 | 🇪🇸 ES | 6239 |
| 3 | 🇮🇳 IN | 5869 |
| 4 | 🇦🇺 AU | 5504 |
| 5 | 🇩🇪 DE | 4892 |
| 6 | 🇮🇹 IT | 4884 |
| 7 | 🇧🇷 BR | 4836 |
| 8 | 🇨🇦 CA | 4396 |
| 9 | 🇯🇵 JP | 4344 |
| 10 | 🇬🇧 GB | 3750 |
| 11 | 🇫🇷 FR | 3519 |
| 12 | 🇨🇴 CO | 2997 |
| 13 | 🇲🇽 MX | 2737 |
| 14 | 🇬🇷 GR | 2554 |
| 15 | 🇳🇴 NO | 2440 |
| 16 | 🇨🇭 CH | 2326 |
| 17 | 🇲🇾 MY | 1973 |
| 18 | 🇿🇦 ZA | 1629 |
| 19 | 🇹🇷 TR | 1598 |
| 20 | 🇳🇿 NZ | 1523 |
| 21 | 🇹🇭 TH | 1518 |
| 22 | 🇵🇱 PL | 1466 |
| 23 | 🇰🇷 KR | 1365 |
| 24 | 🇵🇭 PH | 1357 |
| 25 | 🇬🇹 GT | 1325 |
| 26 | 🇲🇴 MO | 1020 |
| 27 | 🇲🇦 MA | 1017 |
| 28 | 🇲🇪 ME | 911 |
| 29 | 🇳🇱 NL | 895 |
| 30 | 🇭🇷 HR | 793 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1935 |
| 2 | Denver International Airport |  | US | 1472 |
| 3 | Tokyo International Airport |  | JP | 1449 |
| 4 | Indira Gandhi International Airport |  | IN | 1264 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1210 |
| 6 | Harry Reid International Airport |  | US | 1123 |
| 7 | Frankfurt am Main International Airport |  | DE | 1117 |
| 8 | Zurich Airport |  | CH | 1049 |
| 9 | Macau International Airport |  | MO | 1020 |
| 10 | Guaymaral Airport |  | CO | 1017 |
| 11 | La Aurora Airport |  | GT | 1006 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 975 |
| 13 | El Dorado International Airport |  | CO | 957 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 890 |
| 15 | Chicago O'Hare International Airport |  | US | 849 |
| 16 | Madrid Barajas International Airport |  | ES | 798 |
| 17 | Kuala Lumpur International Airport |  | MY | 783 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 756 |
| 19 | Capua Airport |  | IT | 744 |
| 20 | Salt Lake City International Airport |  | US | 733 |
| 21 | Malpensa International Airport |  | IT | 721 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 717 |
| 23 | Bengaluru International Airport |  | IN | 707 |
| 24 | Charles de Gaulle International Airport |  | FR | 686 |
| 25 | Charlotte/Douglas International Airport |  | US | 681 |
| 26 | Congonhas Airport |  | BR | 673 |
| 27 | Tenerife Norte Airport |  | ES | 646 |
| 28 | Daniel K Inouye International Airport |  | US | 645 |
| 29 | Ninoy Aquino International Airport |  | PH | 622 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 596 |
| 31 | Netaji Subhash Chandra Bose International Airport |  | IN | 596 |
| 32 | Barcelona International Airport |  | ES | 595 |
| 33 | General Edward Lawrence Logan International Airport |  | US | 583 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 565 |
| 35 | Vitoria/Foronda Airport |  | ES | 560 |
| 36 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 554 |
| 37 | Don Mueang International Airport |  | TH | 552 |
| 38 | Amsterdam Airport Schiphol |  | NL | 547 |
| 39 | Calgary International Airport |  | CA | 520 |
| 40 | O. R. Tambo International Airport |  | ZA | 514 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 417 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 328 | 21m | 244 km | 1,381.1 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 277 | 1h 7m | 706 km | 3,372.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 243 | 24m | 225 km | 942.7 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 231 | 1h 26m | 910 km | 3,624.9 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 228 | 14m | 114 km | 447.2 t |
| 7 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 227 | 28m | 304 km | 1,190.0 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 224 | 9m | - | - |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 202 | 1h 10m | 770 km | 2,683.4 t |
| 10 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 200 | 31m | - | - |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 194 | 19m | 165 km | 551.8 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 183 | 26m | 275 km | 867.2 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 148 | 21m | 99 km | 253.5 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 136 | 31m | 369 km | 865.7 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 132 | 27m | 152 km | 345.0 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 128 | 27m | 215 km | 474.1 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 128 | 20m | 147 km | 323.9 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 125 | 14m | 154 km | 331.2 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 123 | 23m | 55 km | 116.9 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 122 | 20m | 250 km | 527.0 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 116 | 1h 2m | 695 km | 1,390.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 114 | 18m | 144 km | 283.6 t |
| 25 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 112 | 1h 42m | 1,423 km | 2,748.7 t |
| 27 | Bodø Airport (ENBO) | ENEN (ENEN) | 112 | 13m | - | - |
| 28 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 108 | 12m | - | - |
| 29 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 106 | 1h 41m | 1,156 km | 2,114.7 t |
| 30 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N18NR |  | Meadows Field (KBFL) | Santa Monica Municipal Airport (KSMO) | 2026-05-19 13:23 UTC | 2026-05-19 14:00 UTC | 37m |
| N701NW |  | Las Cruces International Airport (KLRU) | Las Cruces International Airport (KLRU) | 2026-05-19 12:53 UTC | 2026-05-19 14:00 UTC | 1h 7m |
| LXJ447 | LXJ | Waterbury-Oxford Airport (KOXC) | Cincinnati Municipal/Lunken Field (KLUK) | 2026-05-19 12:17 UTC | 2026-05-19 13:59 UTC | 1h 42m |
| VEGA21 | VEG | Enid Woodring Regional Airport (KWDG) | Ramey 1 Airport (0OK8) | 2026-05-19 13:21 UTC | 2026-05-19 13:55 UTC | 34m |
| N275FA |  | Lehigh Valley International Airport (KABE) | Jake Arner Memorial Airport (K22N) | 2026-05-19 13:26 UTC | 2026-05-19 13:49 UTC | 23m |
| N91099 |  | Smith Field (64AR) | Smith Field (64AR) | 2026-05-19 13:33 UTC | 2026-05-19 13:46 UTC | 12m |
| DESERT8 | DES | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | Laguna Army Air Field (Yuma Proving Ground) Airport (KLGF) | 2026-05-19 13:21 UTC | 2026-05-19 13:44 UTC | 22m |
| CXK339 | CXK | Gold Hill Airport (NC25) | Davidson County Executive Airport (KEXX) | 2026-05-19 13:30 UTC | 2026-05-19 13:41 UTC | 11m |
| CXK1067 | CXK | Manassas Regional/Harry P Davis Field (KHEF) | Warrenton/Fauquier Airport (KHWY) | 2026-05-19 13:09 UTC | 2026-05-19 13:40 UTC | 30m |
| EZY9 | easyJet | Dresden Airport (EDDC) | Dresden Airport (EDDC) | 2026-05-19 12:50 UTC | 2026-05-19 13:38 UTC | 48m |
| LLN421 | LLN | Perot Field/Fort Worth Alliance Airport (KAFW) | Decatur Municipal Airport (KLUD) | 2026-05-19 13:18 UTC | 2026-05-19 13:36 UTC | 18m |
| NTF298E | NTF | Václav Havel Airport (LKPR) | Brno-Turany Airport (LKTB) | 2026-05-19 13:01 UTC | 2026-05-19 13:29 UTC | 27m |
| NEW111 | NEW | New Castle Airport (KILG) | L.F. Wade International International Airport (TXKF) | 2026-05-19 11:43 UTC | 2026-05-19 13:27 UTC | 1h 44m |
| CYP111 | CYP | Ben Gurion International Airport (LLBG) | Ben Ya'akov Airport (LLIB) | 2026-05-19 13:12 UTC | 2026-05-19 13:21 UTC | 8m |
| LXJ200 | LXJ | Van Nuys Airport (KVNY) | Porter Ranch Airport (68CN) | 2026-05-19 12:23 UTC | 2026-05-19 13:19 UTC | 56m |
| HK5100G |  | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 2026-05-19 11:40 UTC | 2026-05-19 13:17 UTC | 1h 36m |
| N150XB |  | Blaise Diagne International Airport (GOBD) | Blaise Diagne International Airport (GOBD) | 2026-05-19 13:08 UTC | 2026-05-19 13:15 UTC | 7m |
| EJA529 | EJA | AR55 (AR55) | Barkley Regional Airport (KPAH) | 2026-05-19 12:35 UTC | 2026-05-19 13:13 UTC | 37m |
| N442WT |  | Sioux Gateway/Brig General Bud Day Field (KSUX) | North Central Missouri Regional Airport (KMO8) | 2026-05-19 12:43 UTC | 2026-05-19 13:12 UTC | 28m |
| N812KC |  | Midland International Air And Space Port Airport (KMAF) | City Of Tulia/Swisher County Municipal Airport (KI06) | 2026-05-19 12:48 UTC | 2026-05-19 13:12 UTC | 23m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
