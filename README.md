# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_14:04:25_UTC-green)

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

**Latest saved flight:** 2026-04-15 14:04:25 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-04-15 14:04:25 UTC

- **35,764** saved flights
- **15,666** unique routes
- **121** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **35,764** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **434,863.4 tonnes** estimated CO2 emissions
- **25,209,474 km** total distance flown
- **842 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 1538 |
| 2 | SkyWest Airlines | 1412 |
| 3 | IndiGo | 896 |
| 4 | EJA | 614 |
| 5 | American Airlines | 609 |
| 6 | Southwest Airlines | 507 |
| 7 | ENY | 470 |
| 8 | AXM | 386 |
| 9 | Lufthansa | 382 |
| 10 | LATAM Airlines | 363 |
| 11 | Vueling | 363 |
| 12 | All Nippon Airways | 321 |
| 13 | AZU | 319 |
| 14 | QLK | 302 |
| 15 | Delta Air Lines | 301 |
| 16 | LXJ | 283 |
| 17 | Swiss International | 273 |
| 18 | WIF | 263 |
| 19 | AEE | 241 |
| 20 | easyJet | 240 |
| 21 | Alaska Airlines | 237 |
| 22 | EJU | 233 |
| 23 | VIV | 230 |
| 24 | Japan Airlines | 222 |
| 25 | Air France | 202 |
| 26 | EDV | 201 |
| 27 | United Airlines | 199 |
| 28 | GLO | 193 |
| 29 | AIQ | 190 |
| 30 | JetBlue | 189 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 27889 |
| 2 | 🇮🇳 IN | 2739 |
| 3 | 🇪🇸 ES | 2673 |
| 4 | 🇦🇺 AU | 2545 |
| 5 | 🇧🇷 BR | 2114 |
| 6 | 🇯🇵 JP | 1968 |
| 7 | 🇮🇹 IT | 1923 |
| 8 | 🇩🇪 DE | 1844 |
| 9 | 🇨🇴 CO | 1767 |
| 10 | 🇨🇦 CA | 1732 |
| 11 | 🇬🇧 GB | 1484 |
| 12 | 🇫🇷 FR | 1347 |
| 13 | 🇲🇽 MX | 1134 |
| 14 | 🇬🇷 GR | 1076 |
| 15 | 🇨🇭 CH | 990 |
| 16 | 🇲🇾 MY | 929 |
| 17 | 🇳🇴 NO | 857 |
| 18 | 🇳🇿 NZ | 772 |
| 19 | 🇿🇦 ZA | 754 |
| 20 | 🇵🇭 PH | 685 |
| 21 | 🇹🇭 TH | 666 |
| 22 | 🇹🇷 TR | 652 |
| 23 | 🇬🇹 GT | 617 |
| 24 | 🇰🇷 KR | 611 |
| 25 | 🇵🇱 PL | 566 |
| 26 | 🇲🇦 MA | 448 |
| 27 | 🇳🇱 NL | 353 |
| 28 | 🇲🇪 ME | 349 |
| 29 | 🇧🇸 BS | 346 |
| 30 | 🇮🇩 ID | 345 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 843 |
| 2 | Tokyo International Airport |  | JP | 667 |
| 3 | El Dorado International Airport |  | CO | 630 |
| 4 | Denver International Airport |  | US | 597 |
| 5 | Indira Gandhi International Airport |  | IN | 581 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 529 |
| 7 | Harry Reid International Airport |  | US | 472 |
| 8 | La Aurora Airport |  | GT | 453 |
| 9 | Zurich Airport |  | CH | 444 |
| 10 | Guaymaral Airport |  | CO | 441 |
| 11 | Phoenix Sky Harbor International Airport |  | US | 361 |
| 12 | Kuala Lumpur International Airport |  | MY | 360 |
| 13 | Hartsfield/Jackson Atlanta International Airport |  | US | 356 |
| 14 | Chicago O'Hare International Airport |  | US | 355 |
| 15 | Sydney Kingsford Smith International Airport |  | AU | 345 |
| 16 | Frankfurt am Main International Airport |  | DE | 335 |
| 17 | Madrid Barajas International Airport |  | ES | 323 |
| 18 | Macau International Airport |  | MO | 321 |
| 19 | Charlotte/Douglas International Airport |  | US | 319 |
| 20 | Ninoy Aquino International Airport |  | PH | 317 |
| 21 | Tenerife Norte Airport |  | ES | 317 |
| 22 | Bengaluru International Airport |  | IN | 315 |
| 23 | Congonhas Airport |  | BR | 315 |
| 24 | Malpensa International Airport |  | IT | 293 |
| 25 | Atizapan De Zaragoza Airport |  | MX | 282 |
| 26 | Daniel K Inouye International Airport |  | US | 271 |
| 27 | Salt Lake City International Airport |  | US | 270 |
| 28 | Charles de Gaulle International Airport |  | FR | 266 |
| 29 | Capua Airport |  | IT | 262 |
| 30 | Netaji Subhash Chandra Bose International Airport |  | IN | 253 |
| 31 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 252 |
| 32 | Reno/Tahoe International Airport |  | US | 248 |
| 33 | John Paul II International Airport Kraków-Balice Airport |  | PL | 246 |
| 34 | O. R. Tambo International Airport |  | ZA | 242 |
| 35 | General Edward Lawrence Logan International Airport |  | US | 238 |
| 36 | Barcelona International Airport |  | ES | 234 |
| 37 | Vitoria/Foronda Airport |  | ES | 233 |
| 38 | Viracopos International Airport |  | BR | 225 |
| 39 | Don Mueang International Airport |  | TH | 225 |
| 40 | Seattle-Tacoma International Airport |  | US | 223 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 173 | 25m | - | - |
| 2 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 168 | 1h 8m | 706 km | 2,045.4 t |
| 3 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 147 | 14m | 114 km | 288.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 134 | 24m | 225 km | 519.9 t |
| 5 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 113 | 28m | 304 km | 592.4 t |
| 6 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 104 | 1h 27m | 910 km | 1,632.0 t |
| 7 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 96 | 19m | 165 km | 273.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 91 | 31m | - | - |
| 9 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 87 | 9m | - | - |
| 10 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 85 | 21m | 244 km | 357.9 t |
| 11 | Tokyo International Airport (RJTT) | Okayama Airport (RJOB) | 78 | 54m | 546 km | 734.4 t |
| 12 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 77 | 21m | 99 km | 131.9 t |
| 13 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 76 | 27m | 275 km | 360.1 t |
| 14 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 75 | 1h 11m | 770 km | 996.3 t |
| 15 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 72 | 27m | 152 km | 188.2 t |
| 16 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 69 | 31m | 369 km | 439.2 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 68 | 45m | 452 km | 530.0 t |
| 18 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 67 | 1h 42m | 1,156 km | 1,336.6 t |
| 19 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 60 | 20m | 250 km | 259.2 t |
| 20 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 59 | 52m | 556 km | 565.6 t |
| 21 | Daniel K Inouye International Airport (PHNL) | Hana Airport (PHHN) | 58 | 16m | 206 km | 206.2 t |
| 22 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 58 | 20m | 147 km | 146.8 t |
| 23 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 56 | 14m | 154 km | 148.4 t |
| 24 | El Dorado International Airport (SKBO) | Jose Celestino Mutis Airport (SKQU) | 54 | 13m | 99 km | 92.6 t |
| 25 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 53 | 1h 41m | 1,423 km | 1,300.7 t |
| 26 | Don Mueang International Airport (VTBD) | Prachuap Airport (VTBP) | 53 | 23m | 252 km | 230.1 t |
| 27 | Congonhas Airport (SBSP) | Ubatuba Airport (SDUB) | 53 | 16m | 162 km | 148.6 t |
| 28 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 51 | 26m | 215 km | 188.9 t |
| 29 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 51 | 1h 20m | 961 km | 845.4 t |
| 30 | El Dorado International Airport (SKBO) | Guaymaral Airport (SKGY) | 50 | 12m | 15 km | 13.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N9417Z |  | Brooksville-Tampa Bay Regional Airport (KBKV) | Brooksville-Tampa Bay Regional Airport (KBKV) | 2026-04-15 13:32 UTC | 2026-04-15 14:04 UTC | 32m |
| N481MR |  | Orlando Executive Airport (KORL) | Space Coast Regional Airport (KTIX) | 2026-04-15 13:23 UTC | 2026-04-15 14:03 UTC | 40m |
| N2059C |  | Levelland Municipal Airport (KLLN) | Levelland Municipal Airport (KLLN) | 2026-04-15 13:09 UTC | 2026-04-15 13:59 UTC | 50m |
| PRJOS | PRJ | Centro Nacional de Para-quedismo Airport (SDOI) | Centro Nacional de Para-quedismo Airport (SDOI) | 2026-04-15 13:21 UTC | 2026-04-15 13:58 UTC | 37m |
| N408TW |  | Lakeland Linder International Airport (KLAL) | Lakeland Linder International Airport (KLAL) | 2026-04-15 13:12 UTC | 2026-04-15 13:54 UTC | 41m |
| N520MD |  | Savannah/Hilton Head International Airport (KSAV) | Savannah/Hilton Head International Airport (KSAV) | 2026-04-15 13:51 UTC | 2026-04-15 13:52 UTC | 1m |
| N4303Q |  | Akron Fulton International Airport (KAKR) | Akron Fulton International Airport (KAKR) | 2026-04-15 13:26 UTC | 2026-04-15 13:50 UTC | 24m |
| N784CA |  | Wings Field (KLOM) | Wings Field (KLOM) | 2026-04-15 13:37 UTC | 2026-04-15 13:50 UTC | 13m |
| OKDUI87 | OKD | Mlada Boleslav Airport (LKMB) | Mlada Boleslav Airport (LKMB) | 2026-04-15 13:37 UTC | 2026-04-15 13:49 UTC | 11m |
| N6026Z |  | KFTG (KFTG) | Pueblo Memorial Airport (KPUB) | 2026-04-15 12:52 UTC | 2026-04-15 13:45 UTC | 53m |
| NORSAR6 | NOR | Bergen Airport Flesland (ENBR) | Bergen Airport Flesland (ENBR) | 2026-04-15 13:15 UTC | 2026-04-15 13:43 UTC | 28m |
| HBZWD | HBZ | Courchevel Airport (LFLJ) | Megeve Airport (LFHM) | 2026-04-15 13:27 UTC | 2026-04-15 13:43 UTC | 15m |
| ERU937 | ERU | Daytona Beach International Airport (KDAB) | Daytona Beach International Airport (KDAB) | 2026-04-15 12:33 UTC | 2026-04-15 13:41 UTC | 1h 8m |
| HGB323 | HGB | Narita International Airport (RJAA) | Chek Lap Kok International Airport (VHHH) | 2026-04-15 09:16 UTC | 2026-04-15 13:40 UTC | 4h 24m |
|  |  | Topsail Airpark (01NC) | Camp Davis Mcolf Airport (14NC) | 2026-04-15 13:28 UTC | 2026-04-15 13:39 UTC | 10m |
| KOALA02 | KOA | Ovar Airport (LPOV) | Ovar Airport (LPOV) | 2026-04-15 13:22 UTC | 2026-04-15 13:38 UTC | 16m |
| N541LP |  | Essex County Airport (KCDW) | Lehigh Valley International Airport (KABE) | 2026-04-15 12:51 UTC | 2026-04-15 13:36 UTC | 44m |
| N123UA |  | Sarasota/Bradenton International Airport (KSRQ) | Peter O Knight Airport (KTPF) | 2026-04-15 13:14 UTC | 2026-04-15 13:33 UTC | 18m |
| BBX507 | BBX | Bergen Airport Flesland (ENBR) | Bergen Airport Flesland (ENBR) | 2026-04-15 13:09 UTC | 2026-04-15 13:31 UTC | 22m |
| N12834 |  | Pittsburgh/Butler Regional Airport (KBTP) | Pittsburgh/Butler Regional Airport (KBTP) | 2026-04-15 13:00 UTC | 2026-04-15 13:28 UTC | 28m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
