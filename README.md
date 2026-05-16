# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--16_15:02:01_UTC-green)

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

**Latest saved flight:** 2026-05-16 15:02:01 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-05-16 15:02:01 UTC

- **84,782** saved flights
- **30,503** unique routes
- **130** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **84,782** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,045,619.9 tonnes** estimated CO2 emissions
- **60,615,644 km** total distance flown
- **867 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 3633 |
| 2 | SkyWest Airlines | 3129 |
| 3 | IndiGo | 1832 |
| 4 | EJA | 1595 |
| 5 | American Airlines | 1302 |
| 6 | Southwest Airlines | 1238 |
| 7 | Lufthansa | 1078 |
| 8 | ENY | 1053 |
| 9 | Delta Air Lines | 922 |
| 10 | Vueling | 803 |
| 11 | AXM | 769 |
| 12 | LATAM Airlines | 769 |
| 13 | WIF | 734 |
| 14 | AZU | 665 |
| 15 | All Nippon Airways | 659 |
| 16 | Swiss International | 658 |
| 17 | LXJ | 620 |
| 18 | QLK | 620 |
| 19 | Alaska Airlines | 599 |
| 20 | easyJet | 557 |
| 21 | EJU | 538 |
| 22 | AEE | 533 |
| 23 | Cathay Pacific | 533 |
| 24 | VIV | 507 |
| 25 | Air France | 498 |
| 26 | Japan Airlines | 474 |
| 27 | AXB | 449 |
| 28 | CXK | 448 |
| 29 | MXY | 422 |
| 30 | AIQ | 417 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 69389 |
| 2 | 🇪🇸 ES | 5991 |
| 3 | 🇮🇳 IN | 5731 |
| 4 | 🇦🇺 AU | 5416 |
| 5 | 🇩🇪 DE | 4724 |
| 6 | 🇮🇹 IT | 4677 |
| 7 | 🇧🇷 BR | 4674 |
| 8 | 🇯🇵 JP | 4258 |
| 9 | 🇨🇦 CA | 4209 |
| 10 | 🇬🇧 GB | 3619 |
| 11 | 🇫🇷 FR | 3370 |
| 12 | 🇨🇴 CO | 2836 |
| 13 | 🇲🇽 MX | 2570 |
| 14 | 🇬🇷 GR | 2464 |
| 15 | 🇳🇴 NO | 2371 |
| 16 | 🇨🇭 CH | 2233 |
| 17 | 🇲🇾 MY | 1929 |
| 18 | 🇿🇦 ZA | 1598 |
| 19 | 🇹🇷 TR | 1514 |
| 20 | 🇳🇿 NZ | 1490 |
| 21 | 🇹🇭 TH | 1475 |
| 22 | 🇵🇱 PL | 1410 |
| 23 | 🇵🇭 PH | 1332 |
| 24 | 🇰🇷 KR | 1312 |
| 25 | 🇬🇹 GT | 1277 |
| 26 | 🇲🇦 MA | 983 |
| 27 | 🇲🇴 MO | 982 |
| 28 | 🇲🇪 ME | 887 |
| 29 | 🇳🇱 NL | 863 |
| 30 | 🇭🇷 HR | 758 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 1850 |
| 2 | Tokyo International Airport |  | JP | 1423 |
| 3 | Denver International Airport |  | US | 1422 |
| 4 | Indira Gandhi International Airport |  | IN | 1224 |
| 5 | Eleftherios Venizelos International Airport |  | GR | 1188 |
| 6 | Frankfurt am Main International Airport |  | DE | 1091 |
| 7 | Harry Reid International Airport |  | US | 1067 |
| 8 | Zurich Airport |  | CH | 1006 |
| 9 | Macau International Airport |  | MO | 982 |
| 10 | La Aurora Airport |  | GT | 969 |
| 11 | Guaymaral Airport |  | CO | 956 |
| 12 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 938 |
| 13 | El Dorado International Airport |  | CO | 912 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 850 |
| 15 | Chicago O'Hare International Airport |  | US | 818 |
| 16 | Madrid Barajas International Airport |  | ES | 771 |
| 17 | Kuala Lumpur International Airport |  | MY | 766 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 731 |
| 19 | Malpensa International Airport |  | IT | 707 |
| 20 | Sydney Kingsford Smith International Airport |  | AU | 707 |
| 21 | Salt Lake City International Airport |  | US | 704 |
| 22 | Bengaluru International Airport |  | IN | 699 |
| 23 | Capua Airport |  | IT | 692 |
| 24 | Charles de Gaulle International Airport |  | FR | 663 |
| 25 | Charlotte/Douglas International Airport |  | US | 659 |
| 26 | Congonhas Airport |  | BR | 658 |
| 27 | Daniel K Inouye International Airport |  | US | 617 |
| 28 | Tenerife Norte Airport |  | ES | 615 |
| 29 | Ninoy Aquino International Airport |  | PH | 610 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 594 |
| 31 | Atizapan De Zaragoza Airport |  | MX | 571 |
| 32 | General Edward Lawrence Logan International Airport |  | US | 567 |
| 33 | Barcelona International Airport |  | ES | 566 |
| 34 | John Paul II International Airport Kraków-Balice Airport |  | PL | 548 |
| 35 | Vitoria/Foronda Airport |  | ES | 538 |
| 36 | Don Mueang International Airport |  | TH | 534 |
| 37 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 534 |
| 38 | Amsterdam Airport Schiphol |  | NL | 524 |
| 39 | O. R. Tambo International Airport |  | ZA | 504 |
| 40 | Calgary International Airport |  | CA | 494 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 396 | 26m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 313 | 21m | 244 km | 1,318.0 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 275 | 1h 7m | 706 km | 3,348.1 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 240 | 24m | 225 km | 931.1 t |
| 5 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 225 | 1h 26m | 910 km | 3,530.8 t |
| 6 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 224 | 28m | 304 km | 1,174.3 t |
| 7 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 218 | 14m | 114 km | 427.6 t |
| 8 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 216 | 9m | - | - |
| 9 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 199 | 31m | - | - |
| 10 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 193 | 1h 11m | 770 km | 2,563.9 t |
| 11 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 192 | 19m | 165 km | 546.1 t |
| 12 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 177 | 26m | 275 km | 838.7 t |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 144 | 20m | 99 km | 246.7 t |
| 14 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 140 | 44m | 452 km | 1,091.1 t |
| 15 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 133 | 31m | 369 km | 846.6 t |
| 16 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 127 | 27m | 152 km | 331.9 t |
| 17 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 126 | 27m | 215 km | 466.7 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 124 | 20m | 147 km | 313.8 t |
| 19 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 122 | 14m | 154 km | 323.3 t |
| 20 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 121 | 23m | 55 km | 115.0 t |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 119 | 20m | 250 km | 514.0 t |
| 22 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 115 | 1h 2m | 695 km | 1,378.5 t |
| 23 | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | Minneapolis-St Paul International/Wold-Chamberlain Airport (KMSP) | 114 | 57m | - | - |
| 24 | Netaji Subhash Chandra Bose International Airport (VECC) | Shillong Airport (VEBI) | 113 | 57m | 493 km | 961.4 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 108 | 1h 43m | 1,423 km | 2,650.5 t |
| 26 | Bodø Airport (ENBO) | ENEN (ENEN) | 108 | 13m | - | - |
| 27 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 107 | 18m | 144 km | 266.2 t |
| 28 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 106 | 54m | 546 km | 998.0 t |
| 29 | Tenerife Norte Airport (GCXO) | Tenerife Norte Airport (GCXO) | 104 | 12m | - | - |
| 30 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 101 | 1h 41m | 1,156 km | 2,014.9 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N554SC |  | Christmas Flying Service Airport (MS03) | Shelby Air Service Airport (93MS) | 2026-05-16 14:36 UTC | 2026-05-16 15:02 UTC | 25m |
| CAP1622 | CAP | KL38 (KL38) | KL38 (KL38) | 2026-05-16 14:11 UTC | 2026-05-16 15:01 UTC | 50m |
| N64DG |  | Blair Executive Airport (KBTA) | Lincoln Airport (KLNK) | 2026-05-16 14:41 UTC | 2026-05-16 14:54 UTC | 12m |
| SWR166M | Swiss International | Munich International Airport (EDDM) | Zurich Airport (LSZH) | 2026-05-16 14:21 UTC | 2026-05-16 14:54 UTC | 32m |
| N543LK |  | Leesburg Executive Airport (KJYO) | Ocean City Municipal Airport (KOXB) | 2026-05-16 14:01 UTC | 2026-05-16 14:52 UTC | 51m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-05-16 13:59 UTC | 2026-05-16 14:50 UTC | 50m |
| N98DA |  | Manassas Regional/Harry P Davis Field (KHEF) | Warrenton/Fauquier Airport (KHWY) | 2026-05-16 14:35 UTC | 2026-05-16 14:42 UTC | 6m |
| N570FG |  | Doylestown Airport (KDYL) | Doylestown Airport (KDYL) | 2026-05-16 14:31 UTC | 2026-05-16 14:40 UTC | 9m |
| N253MM |  | KA50 (KA50) | Lone Tree Ranch Airport (35CO) | 2026-05-16 14:19 UTC | 2026-05-16 14:40 UTC | 20m |
| N408GG |  | Newark Liberty International Airport (KEWR) | Newark Liberty International Airport (KEWR) | 2026-05-16 14:12 UTC | 2026-05-16 14:38 UTC | 25m |
| N376VR |  | New Bedford Regional Airport (KEWB) | Plymouth Municipal Airport (KPYM) | 2026-05-16 14:22 UTC | 2026-05-16 14:35 UTC | 13m |
| N7DW |  | Lee Airport (KANP) | MD09 (MD09) | 2026-05-16 14:21 UTC | 2026-05-16 14:34 UTC | 13m |
| N685DW |  | Lebanon Municipal Airport (KLEB) | Lebanon Municipal Airport (KLEB) | 2026-05-16 13:52 UTC | 2026-05-16 14:34 UTC | 42m |
| SPTN622 | SPT | Van Vleck Airport (57CN) | Sacramento Mather Airport (KMHR) | 2026-05-16 14:14 UTC | 2026-05-16 14:32 UTC | 17m |
| DEDNE | DED | Gunzburg-Donauried Airport (EDMG) | Aalen-Heidenheim/Elchingen Airport (EDPA) | 2026-05-16 14:18 UTC | 2026-05-16 14:30 UTC | 12m |
| CXK426 | CXK | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 2026-05-16 14:09 UTC | 2026-05-16 14:30 UTC | 20m |
| N5462Q |  | Roberts Field (KRDM) | Bend Municipal Airport (KBDN) | 2026-05-16 14:02 UTC | 2026-05-16 14:27 UTC | 24m |
| N8175P |  | La Cholla Airpark (57AZ) | 4AZ7 (4AZ7) | 2026-05-16 14:00 UTC | 2026-05-16 14:27 UTC | 26m |
| N91PR |  | Thorson Airfield (SD05) | 3SD6 (3SD6) | 2026-05-16 13:57 UTC | 2026-05-16 14:27 UTC | 29m |
| N8493F |  | Mason City Municipal Airport (KMCW) | Mason City Municipal Airport (KMCW) | 2026-05-16 14:13 UTC | 2026-05-16 14:26 UTC | 12m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
