# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_22:27:09_UTC-green)

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

**Latest saved flight:** 2026-06-05 22:27:09 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-06-05 22:27:09 UTC

- **103,204** saved flights
- **36,523** unique routes
- **133** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **103,204** saved routes in the archive
- **1h 15m** average flight duration

### Carbon Footprint Estimate

- **1,260,267.2 tonnes** estimated CO2 emissions
- **73,058,968 km** total distance flown
- **861 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 4238 |
| 2 | SkyWest Airlines | 3887 |
| 3 | IndiGo | 2059 |
| 4 | EJA | 1976 |
| 5 | American Airlines | 1669 |
| 6 | Southwest Airlines | 1561 |
| 7 | ENY | 1282 |
| 8 | Delta Air Lines | 1218 |
| 9 | Lufthansa | 1191 |
| 10 | Vueling | 952 |
| 11 | LATAM Airlines | 914 |
| 12 | WIF | 907 |
| 13 | AXM | 886 |
| 14 | AZU | 829 |
| 15 | LXJ | 781 |
| 16 | Swiss International | 744 |
| 17 | All Nippon Airways | 727 |
| 18 | Alaska Airlines | 722 |
| 19 | QLK | 693 |
| 20 | easyJet | 669 |
| 21 | EJU | 645 |
| 22 | Cathay Pacific | 618 |
| 23 | AEE | 600 |
| 24 | VIV | 592 |
| 25 | Air France | 590 |
| 26 | United Airlines | 572 |
| 27 | MXY | 559 |
| 28 | CXK | 553 |
| 29 | Japan Airlines | 511 |
| 30 | AXB | 506 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 86923 |
| 2 | 🇪🇸 ES | 7089 |
| 3 | 🇮🇳 IN | 6505 |
| 4 | 🇦🇺 AU | 6270 |
| 5 | 🇧🇷 BR | 5644 |
| 6 | 🇩🇪 DE | 5540 |
| 7 | 🇮🇹 IT | 5470 |
| 8 | 🇨🇦 CA | 5376 |
| 9 | 🇯🇵 JP | 4752 |
| 10 | 🇬🇧 GB | 4350 |
| 11 | 🇫🇷 FR | 4089 |
| 12 | 🇨🇴 CO | 3543 |
| 13 | 🇲🇽 MX | 3102 |
| 14 | 🇬🇷 GR | 2935 |
| 15 | 🇳🇴 NO | 2872 |
| 16 | 🇨🇭 CH | 2639 |
| 17 | 🇲🇾 MY | 2259 |
| 18 | 🇹🇷 TR | 1952 |
| 19 | 🇿🇦 ZA | 1790 |
| 20 | 🇳🇿 NZ | 1733 |
| 21 | 🇹🇭 TH | 1701 |
| 22 | 🇰🇷 KR | 1677 |
| 23 | 🇵🇱 PL | 1648 |
| 24 | 🇬🇹 GT | 1507 |
| 25 | 🇵🇭 PH | 1506 |
| 26 | 🇲🇦 MA | 1138 |
| 27 | 🇲🇴 MO | 1078 |
| 28 | 🇳🇱 NL | 1017 |
| 29 | 🇲🇪 ME | 970 |
| 30 | 🇭🇷 HR | 903 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 2242 |
| 2 | Denver International Airport |  | US | 1771 |
| 3 | Tokyo International Airport |  | JP | 1577 |
| 4 | Indira Gandhi International Airport |  | IN | 1411 |
| 5 | Harry Reid International Airport |  | US | 1326 |
| 6 | Eleftherios Venizelos International Airport |  | GR | 1316 |
| 7 | Guaymaral Airport |  | CO | 1287 |
| 8 | Frankfurt am Main International Airport |  | DE | 1191 |
| 9 | Zurich Airport |  | CH | 1173 |
| 10 | La Aurora Airport |  | GT | 1160 |
| 11 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 1118 |
| 12 | El Dorado International Airport |  | CO | 1083 |
| 13 | Macau International Airport |  | MO | 1078 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1044 |
| 15 | Chicago O'Hare International Airport |  | US | 1032 |
| 16 | Madrid Barajas International Airport |  | ES | 899 |
| 17 | Kuala Lumpur International Airport |  | MY | 891 |
| 18 | Hartsfield/Jackson Atlanta International Airport |  | US | 887 |
| 19 | Salt Lake City International Airport |  | US | 872 |
| 20 | Capua Airport |  | IT | 856 |
| 21 | Charlotte/Douglas International Airport |  | US | 804 |
| 22 | Sydney Kingsford Smith International Airport |  | AU | 799 |
| 23 | Charles de Gaulle International Airport |  | FR | 785 |
| 24 | Congonhas Airport |  | BR | 783 |
| 25 | Bengaluru International Airport |  | IN | 779 |
| 26 | Malpensa International Airport |  | IT | 775 |
| 27 | Daniel K Inouye International Airport |  | US | 710 |
| 28 | Tenerife Norte Airport |  | ES | 703 |
| 29 | Ninoy Aquino International Airport |  | PH | 688 |
| 30 | Barcelona International Airport |  | ES | 678 |
| 31 | General Edward Lawrence Logan International Airport |  | US | 671 |
| 32 | Atizapan De Zaragoza Airport |  | MX | 666 |
| 33 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 662 |
| 34 | Amsterdam Airport Schiphol |  | NL | 629 |
| 35 | Don Mueang International Airport |  | TH | 623 |
| 36 | Vitoria/Foronda Airport |  | ES | 621 |
| 37 | Calgary International Airport |  | CA | 615 |
| 38 | Netaji Subhash Chandra Bose International Airport |  | IN | 602 |
| 39 | Seattle-Tacoma International Airport |  | US | 600 |
| 40 | Norman Y Mineta San Jose International Airport |  | US | 585 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 531 | 25m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 378 | 21m | 244 km | 1,591.7 t |
| 3 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 279 | 1h 7m | 706 km | 3,396.8 t |
| 4 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 272 | 9m | - | - |
| 5 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 270 | 24m | 225 km | 1,047.5 t |
| 6 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 257 | 14m | 114 km | 504.1 t |
| 7 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 251 | 1h 26m | 910 km | 3,938.8 t |
| 8 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 249 | 28m | 304 km | 1,305.3 t |
| 9 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 237 | 1h 10m | 770 km | 3,148.4 t |
| 10 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 216 | 19m | 165 km | 614.4 t |
| 11 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 204 | 26m | 275 km | 966.7 t |
| 12 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 203 | 31m | - | - |
| 13 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 159 | 20m | 99 km | 272.4 t |
| 14 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 155 | 22m | 55 km | 147.3 t |
| 15 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 150 | 27m | 215 km | 555.5 t |
| 16 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 147 | 14m | 154 km | 389.5 t |
| 17 | Tokyo International Airport (RJTT) | Tajima Airport (RJBT) | 144 | 44m | 452 km | 1,122.3 t |
| 18 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 144 | 27m | 152 km | 376.3 t |
| 19 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 143 | 31m | 369 km | 910.2 t |
| 20 | Bodø Airport (ENBO) | ENEN (ENEN) | 139 | 13m | - | - |
| 21 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 138 | 20m | 250 km | 596.1 t |
| 22 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 134 | 18m | 144 km | 333.3 t |
| 23 | Eleftherios Venizelos International Airport (LGAV) | Paros Airport (LGPA) | 132 | 20m | 147 km | 334.0 t |
| 24 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 129 | 1h 39m | 1,156 km | 2,573.5 t |
| 25 | General Mariano Escobedo International Airport (MMMY) | Atizapan De Zaragoza Airport (MMJC) | 128 | 1h 1m | 695 km | 1,534.3 t |
| 26 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 120 | 1h 43m | 1,423 km | 2,945.0 t |
| 27 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 120 | 12m | - | - |
| 28 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 118 | 1h 18m | 961 km | 1,955.9 t |
| 29 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 118 | 44m | 241 km | 490.1 t |
| 30 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 117 | 1h 52m | 1,304 km | 2,632.2 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| N4431R |  | Princeton Airport (K39N) | Princeton Airport (K39N) | 2026-06-05 22:10 UTC | 2026-06-05 22:27 UTC | 16m |
| N1026V |  | Ted Stevens Anchorage International Airport (PANC) | Kenai Municipal Airport (PAEN) | 2026-06-05 21:54 UTC | 2026-06-05 22:21 UTC | 26m |
| N1587U |  | King Salmon Airport (PAKN) | Igiugig Airport (PAIG) | 2026-06-05 21:45 UTC | 2026-06-05 22:13 UTC | 28m |
| N27DX |  | Teterboro Airport (KTEB) | Laguardia Airport (KLGA) | 2026-06-05 21:05 UTC | 2026-06-05 22:13 UTC | 1h 7m |
|  |  | Keller Airfield (5AR7) | Keller Airfield (5AR7) | 2026-06-05 22:12 UTC | 2026-06-05 22:12 UTC | 0m |
| SRN6911 | SRN | Kaunas International Airport (EYKA) | Cologne Bonn Airport (EDDK) | 2026-06-05 19:13 UTC | 2026-06-05 22:09 UTC | 2h 56m |
| ACW2730 | ACW | Teterboro Airport (KTEB) | General Mariano Escobedo International Airport (MMMY) | 2026-06-05 17:48 UTC | 2026-06-05 22:06 UTC | 4h 17m |
| N555JM |  | St Bernard Field (94NY) | Murphy Field (06NY) | 2026-06-05 21:57 UTC | 2026-06-05 22:06 UTC | 8m |
| N739BZ |  | Cheyenne Regional/Jerry Olson Field (KCYS) | Vowers Ranch Airport (WY29) | 2026-06-05 21:54 UTC | 2026-06-05 22:05 UTC | 11m |
| N555NL |  | John F Kennedy International Airport (KJFK) | Laguardia Airport (KLGA) | 2026-06-05 21:53 UTC | 2026-06-05 22:05 UTC | 12m |
| N40230 |  | Sky Ranch Airport (TN98) | Sky Ranch Airport (TN98) | 2026-06-05 22:01 UTC | 2026-06-05 22:05 UTC | 3m |
| N60WP |  | Redding Regional Airport (KRDD) | Lonnie Pool Field/Weaverville Airport (KO54) | 2026-06-05 21:50 UTC | 2026-06-05 22:02 UTC | 12m |
| GEC8466 | GEC | Juhu Aerodrome (VAJJ) | Macau International Airport (VMMC) | 2026-06-05 17:05 UTC | 2026-06-05 22:00 UTC | 4h 55m |
| N800BD |  | Whitaker Airport (MS43) | Central Colorado Regional Airport (KAEJ) | 2026-06-05 19:55 UTC | 2026-06-05 21:59 UTC | 2h 4m |
| N950TT |  | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 2026-06-05 21:38 UTC | 2026-06-05 21:57 UTC | 18m |
| N682AC |  | Garrett Ranch Airport (77XS) | Bb Airpark (TE88) | 2026-06-05 21:45 UTC | 2026-06-05 21:56 UTC | 11m |
| N510PR |  | Talkeetna Airport (PATK) | Helio Airport (2AK7) | 2026-06-05 21:20 UTC | 2026-06-05 21:55 UTC | 35m |
| N7374P |  | Oakland San Francisco Bay Airport (KOAK) | Truckee-Tahoe Airport (KTRK) | 2026-06-05 20:49 UTC | 2026-06-05 21:55 UTC | 1h 5m |
| N805KG |  | Laurence G Hanscom Field (KBED) | Newark Liberty International Airport (KEWR) | 2026-06-05 20:44 UTC | 2026-06-05 21:54 UTC | 1h 10m |
| N616SP |  | Crosswinds-Wilson Pvt Airport (SC37) | Mercer County Airport (KBLF) | 2026-06-05 20:27 UTC | 2026-06-05 21:52 UTC | 1h 24m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
