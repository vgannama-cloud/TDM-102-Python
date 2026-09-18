{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "be02a957-7133-4d02-818e-fedeb3cecb05",
   "metadata": {},
   "source": [
    "# Project 8 -- Vinay Gannamaneni"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1228853-dd19-4ab2-89e0-0394d7d72de3",
   "metadata": {},
   "source": [
    "**TA Help:** (for instance) John Smith, Alice Jones, etc., list names of any TAs who helped you\n",
    "\n",
    "- For example: Help with figuring out how to write a function (describe the tasks that they helped you with)\n",
    "\n",
    "**Collaboration:** My Friend in CS, My Uncle, Another Student, etc., list names of any other people who helped you\n",
    "\n",
    "(describe the tasks that they helped you with)\n",
    "- For example: helped figuring out how to load the dataset.\n",
    "- Another example: helped debug error with my plot.\n",
    "\n",
    "**Internet Resources:** Stack Exchange, Stack Overflow, etc.\n",
    "\n",
    "(describe any information that you learned from internet resources, including the URLs)\n",
    "- data frames in Pandas versus R from StackOverflow  https://stackoverflow.com/questions/8991709/why-were-pandas-merges-in-python-faster-than-data-table-merges-in-r-in-2012\n",
    "\n",
    "**ChatGPT, Gemini, Claude, etc:** Any language models or generative AI chatbots that helped you.\n",
    "\n",
    "(if you used any such tools, please tell us here)\n",
    "- For example:  I asked ChatGPT how to define a new data frames\n",
    "- Another example:  Gemini told me how to make a function for sorting my data\n",
    "\n",
    "- ***Link to AI Chat History***: Please share a link to your chat if you used AI (ex. ChatGPT Shared Links)\n",
    "**OVERALL MESSAGE:** Any time that you used anything except your brain to solve the questions in these projects, you need to disclose such resources at the start of the project, with details about your usage of the tools.\n",
    "\n",
    "**YOUR OWN WORK:** Even when you utilize other resources, do NOT just copy and paste.  Write all explanations in your own words, using several sentences in English, which are understandable and which you wrote (and did not just copy and paste)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6180e742-8e39-4698-98ff-5b00c8cf8ea0",
   "metadata": {},
   "source": [
    "## Custom functions to filter songs by energy level and by album"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4faa2e61-4c3a-4673-821a-9fdbefb3e10b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "pd.set_option('display.max_columns', None)\n",
    "ts_songs = pd.read_csv('/anvil/projects/tdm/data/spotify/taylor_swift_discography_updated.csv', sep=\";\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b456e57c-4a12-464b-999a-ef2df5af80c1",
   "metadata": {},
   "source": [
    "Setting display options and loading in data set"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cfb75ab9-6f47-4c7d-bd79-9a9f58280e0e",
   "metadata": {},
   "source": [
    "To find min and max levels"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b99f6752-54c5-46be-93dd-4aea36cbb385",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Maximum energy level: 0.95\n",
      "Minimum energy level: 0.118\n"
     ]
    }
   ],
   "source": [
    "max_energy = ts_songs['energy'].max()\n",
    "min_energy = ts_songs['energy'].min()\n",
    "print(f\"Maximum energy level: {max_energy}\")\n",
    "print(f\"Minimum energy level: {min_energy}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "34dcb715-64c6-418a-b248-ac9dba491d3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of high energy songs (>= 0.57): 289\n"
     ]
    }
   ],
   "source": [
    "def find_songs_with_energy(input_df, threshold):\n",
    "    my_output = input_df[input_df[\"energy\"] >= threshold]\n",
    "    return my_output\n",
    "\n",
    "my_median = ts_songs['energy'].median()\n",
    "high_energy_df = find_songs_with_energy(ts_songs, my_median)\n",
    "\n",
    "print(f\"Number of high energy songs (>= {my_median}): {len(high_energy_df)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7200d326-49a9-4b07-9d96-098240a7b65c",
   "metadata": {},
   "source": [
    "Define energy filter function and calculte median to test function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c3fe1dda-b5e8-402a-b171-0c454bb15873",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Songs in TTPD Anthology: 31\n",
      "                             track_name  \\\n",
      "0         Fortnight (feat. Post Malone)   \n",
      "1         The Tortured Poets Department   \n",
      "2  My Boy Only Breaks His Favorite Toys   \n",
      "3                              Down Bad   \n",
      "4                       So Long, London   \n",
      "\n",
      "                                          album  \n",
      "0  The Tortured Poets Department: The Anthology  \n",
      "1  The Tortured Poets Department: The Anthology  \n",
      "2  The Tortured Poets Department: The Anthology  \n",
      "3  The Tortured Poets Department: The Anthology  \n",
      "4  The Tortured Poets Department: The Anthology  \n"
     ]
    }
   ],
   "source": [
    "def find_songs_by_album(input_df, album_name):\n",
    "    my_output = input_df[input_df[\"album\"] == album_name]\n",
    "    return my_output\n",
    "\n",
    "ttpd_songs = find_songs_by_album(ts_songs, \"The Tortured Poets Department: The Anthology\")\n",
    "print(f\"Songs in TTPD Anthology: {len(ttpd_songs)}\")\n",
    "print(ttpd_songs[['track_name', 'album']].head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f922cfec-80ea-47b4-958d-543b8fe2fecd",
   "metadata": {},
   "source": [
    "Define album filter function and test function"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc601975-35ed-4680-a4e1-0273ee3cc047",
   "metadata": {},
   "source": [
    "## Converting song duration and finding albums over a length threshold"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a16336a1-1ef0-41e8-bc7c-49387db27497",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                             track_name  duration_ms  duration_min\n",
      "0         Fortnight (feat. Post Malone)       228965      3.816083\n",
      "1         The Tortured Poets Department       293048      4.884133\n",
      "2  My Boy Only Breaks His Favorite Toys       203801      3.396683\n",
      "3                              Down Bad       261228      4.353800\n",
      "4                       So Long, London       262974      4.382900\n"
     ]
    }
   ],
   "source": [
    "ts_songs['duration_sec'] = ts_songs['duration_ms'] / 1000\n",
    "ts_songs['duration_min'] = ts_songs['duration_sec'] / 60\n",
    "\n",
    "print(ts_songs[['track_name', 'duration_ms', 'duration_min']].head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14dc22d4-ddc3-41cc-a91a-cb0025bc0c80",
   "metadata": {},
   "source": [
    "Created new duration columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "087e67ec-05a2-467a-b614-48d2785cfa51",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Albums longer than 80 minutes:\n",
      "                                                album  duration_min\n",
      "3                    1989 (Taylor's Version) [Deluxe]     81.301667\n",
      "5                         Fearless (Taylor's Version)    106.541500\n",
      "11                   Midnights (The Til Dawn Edition)     80.586083\n",
      "13                               Red (Deluxe Edition)     90.217667\n",
      "14                             Red (Taylor's Version)    130.663833\n",
      "16                         Speak Now (Deluxe Edition)     91.840117\n",
      "17                       Speak Now (Taylor's Version)    104.734183\n",
      "21       The Tortured Poets Department: The Anthology    122.645733\n",
      "26  folklore: the long pond studio sessions (from ...    134.704517\n",
      "28     reputation Stadium Tour Surprise Song Playlist    186.266467\n"
     ]
    }
   ],
   "source": [
    "def find_albums_by_time(input_df, input_min_duration):\n",
    "    total_by_album = input_df.groupby(\"album\")[\"duration_min\"].sum().reset_index()\n",
    "    long_albums = total_by_album[total_by_album[\"duration_min\"] > input_min_duration]\n",
    "    return long_albums\n",
    "\n",
    "albums_80 = find_albums_by_time(ts_songs, 80)\n",
    "print(\"Albums longer than 80 minutes:\")\n",
    "print(albums_80)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4bc2123d-1930-4e6b-89c9-fec0461688e6",
   "metadata": {},
   "source": [
    "Defining the function to find albums by total time. Group by album and sum duration and filter for albums longer than the threshold"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f1f68030-3565-49e6-a494-7d1908e28e94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Albums longer than 120 minutes:\n",
      "                                                album  duration_min\n",
      "14                             Red (Taylor's Version)    130.663833\n",
      "21       The Tortured Poets Department: The Anthology    122.645733\n",
      "26  folklore: the long pond studio sessions (from ...    134.704517\n",
      "28     reputation Stadium Tour Surprise Song Playlist    186.266467\n"
     ]
    }
   ],
   "source": [
    "albums_120 = find_albums_by_time(ts_songs, 120)\n",
    "print(\"Albums longer than 120 minutes:\")\n",
    "print(albums_120)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb8fe27f-2e16-4e12-94de-5a69d89c632e",
   "metadata": {},
   "source": [
    "Now tested with 120 minutes instead of 80 minutes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e586edd-ff26-4ce2-8f6b-2424b26f2929",
   "metadata": {},
   "source": [
    "## Classifying albums as short, medium or long by total duration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fbb69f01-4cdd-4d0b-89e9-b6f88f612e1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "lower_threshold = 30\n",
    "upper_threshold = 80"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47c6229f-35f7-400c-8366-c442baa5cf47",
   "metadata": {},
   "source": [
    "We set upper and lower thresholds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6fceb4ac-1934-49c7-a464-b4111d5a532a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                              album  duration_min              category\n",
      "0                              1989     48.797733        Standard Album\n",
      "1             1989 (Deluxe Edition)     68.760800        Standard Album\n",
      "2           1989 (Taylor's Version)     77.972117        Standard Album\n",
      "3  1989 (Taylor's Version) [Deluxe]     81.301667  Long Album/Anthology\n",
      "4                          Fearless     53.547900        Standard Album\n"
     ]
    }
   ],
   "source": [
    "total_by_album = ts_songs.groupby(\"album\")[\"duration_min\"].sum().reset_index()\n",
    "\n",
    "def my_classify(my_time_length):\n",
    "    if my_time_length < lower_threshold:\n",
    "        return \"EP/Short Album\"\n",
    "    elif my_time_length > upper_threshold:\n",
    "        return \"Long Album/Anthology\"\n",
    "    else:\n",
    "        return \"Standard Album\"\n",
    "\n",
    "total_by_album[\"category\"] = total_by_album[\"duration_min\"].apply(my_classify)\n",
    "print(total_by_album.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f398096-f88d-4872-9af0-e01342158899",
   "metadata": {},
   "source": [
    "Building logic outside function structure first"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "01ff6390-0912-47ec-bb5a-77d16fb1b42f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                              album  duration_min        category\n",
      "0                              1989     48.797733  standard_album\n",
      "1             1989 (Deluxe Edition)     68.760800  standard_album\n",
      "2           1989 (Taylor's Version)     77.972117  standard_album\n",
      "3  1989 (Taylor's Version) [Deluxe]     81.301667      long_album\n",
      "4                          Fearless     53.547900  standard_album\n"
     ]
    }
   ],
   "source": [
    "# Defining the comprehensive function\n",
    "def albums_by_length(df, lower_threshold, upper_threshold):\n",
    "    total_by_album = df.groupby(\"album\")[\"duration_min\"].sum().reset_index()\n",
    "\n",
    "    def classify(duration):\n",
    "        if duration < lower_threshold:\n",
    "            return \"short_album\"\n",
    "        elif duration > upper_threshold:\n",
    "            return \"long_album\"\n",
    "        else:\n",
    "            return \"standard_album\"\n",
    "\n",
    "    total_by_album[\"category\"] = total_by_album[\"duration_min\"].apply(classify)\n",
    "    return total_by_album\n",
    "\n",
    "# Testing the function\n",
    "test_results = albums_by_length(ts_songs, lower_threshold=30, upper_threshold=80)\n",
    "print(test_results.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1dd35b45-8894-4b33-9272-308ae2a75d03",
   "metadata": {},
   "source": [
    "Defining the comprehensive function and testing"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "da22f29c-d245-4d2b-9fc1-ca14cb6087d9",
   "metadata": {},
   "source": [
    "## Cleaning video counts and aggregating by YouTube category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a7d98731-d1f9-4eeb-988d-6a4ac0886335",
   "metadata": {},
   "outputs": [],
   "source": [
    "youtubers = pd.read_csv('/anvil/projects/tdm/data/youtube/most_subscribed_youtube_channels.csv')\n",
    "\n",
    "youtubers['video_count2'] = pd.to_numeric(youtubers['video count'].str.replace(\",\", \"\", regex=False))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96304863-5732-478b-ba70-c46bd428bcc6",
   "metadata": {},
   "source": [
    "Reading the data set and cleaning the video count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e68f6b47-ec2b-4b30-96ef-28e232267c11",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "category\n",
      "Autos & Vehicles            2874\n",
      "Comedy                     93562\n",
      "Education                 124727\n",
      "Entertainment            2674176\n",
      "Film & Animation          133319\n",
      "Gaming                    427292\n",
      "Howto & Style              81419\n",
      "Movies                      5576\n",
      "Music                     510337\n",
      "News & Politics          2754693\n",
      "Nonprofits & Activism     188445\n",
      "People & Blogs           1045091\n",
      "Pets & Animals             23960\n",
      "Science & Technology       36622\n",
      "Shows                     283027\n",
      "Sports                    140464\n",
      "Trailers                   13613\n",
      "Travel & Events              632\n",
      "Name: video_count2, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "video_count_per_genre = youtubers.groupby(\"category\")[\"video_count2\"].sum()\n",
    "print(video_count_per_genre)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0d552245-b4d6-474a-9cc9-fa7b8e674d55",
   "metadata": {},
   "source": [
    "Grouping youtubers by category"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5b651b4f-bdda-4f15-87e7-789b7874a660",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "started      2005      2006     2007     2008     2009     2010     2011  \\\n",
      "category                                                                   \n",
      "Gaming    17878.0  163116.0  11967.0  16356.0  15342.0   9998.0  27421.0   \n",
      "Music      1446.0   36423.0  51621.0  33451.0  16392.0  31766.0  89353.0   \n",
      "\n",
      "started      2012     2013      2014    2015    2016    2017    2018    2019  \\\n",
      "category                                                                       \n",
      "Gaming    72858.0  32267.0   31332.0  7342.0  7903.0  9302.0  2952.0  1126.0   \n",
      "Music     44299.0  71681.0  119692.0  5447.0  8477.0   156.0   121.0    12.0   \n",
      "\n",
      "started    2020  \n",
      "category         \n",
      "Gaming    132.0  \n",
      "Music       NaN  \n"
     ]
    }
   ],
   "source": [
    "gm_subset = youtubers[youtubers[\"category\"].isin([\"Gaming\", \"Music\"])]\n",
    "\n",
    "grouped_counts = gm_subset.groupby([\"category\", \"started\"])[\"video_count2\"].sum().unstack()\n",
    "print(grouped_counts)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9ac5f99-db07-48c1-bf36-0fff2bfa6b42",
   "metadata": {},
   "source": [
    "Filter for specific categories and group by two columns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "88c9cdac-3e92-498f-83fa-e089bfc44ac8",
   "metadata": {},
   "source": [
    "## Finding the top YouTuber by subscribers within a genre"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "65a2ea39-7aab-4550-8f5e-ec97cee47581",
   "metadata": {},
   "outputs": [],
   "source": [
    "youtubers['subscribers2'] = pd.to_numeric(youtubers['subscribers'].str.replace(\",\", \"\", regex=False))\n",
    "\n",
    "def top_youtuber_by_genre(input_df, genre):\n",
    "    genre_rows = input_df[input_df[\"category\"] == genre]\n",
    "    top_index = genre_rows['subscribers2'].idxmax()\n",
    "    return genre_rows.loc[top_index]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9fbf00fb-2418-460f-ae94-2a32b0c28952",
   "metadata": {},
   "source": [
    "Clean the subscribers column and make a function to find top youtuber in a genre"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "39bf48cc-f044-47db-95e7-e7fddabf4673",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Top Gaming YouTuber:\n",
      "Youtuber        PewDiePie\n",
      "subscribers2    111000000\n",
      "Name: 5, dtype: object\n"
     ]
    }
   ],
   "source": [
    "top_gaming = top_youtuber_by_genre(youtubers, \"Gaming\")\n",
    "print(\"Top Gaming YouTuber:\")\n",
    "print(top_gaming[['Youtuber', 'subscribers2']])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f589399f-591a-4bb2-8aaa-beb2f3ad24ea",
   "metadata": {},
   "source": [
    "Testing with Gaming and then Music"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1098c638-8728-457a-8669-9f26a75c1f86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Top Music YouTuber:\n",
      "Youtuber         T-Series\n",
      "subscribers2    222000000\n",
      "Name: 0, dtype: object\n"
     ]
    }
   ],
   "source": [
    "top_music = top_youtuber_by_genre(youtubers, \"Music\")\n",
    "print(\"\\nTop Music YouTuber:\")\n",
    "print(top_music[['Youtuber', 'subscribers2']])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17fa30d7-8503-4261-9dd0-1a7b9ff65d23",
   "metadata": {},
   "source": [
    "This dataset from 3 years ago lists PewDiePie as the top gaming creator. However, the landscape has shifted significantly by 2026. As mentioned in the context, MrBeast has since surpassed all individual creators, reaching over 400 million subscribers. While the categories (Music, Gaming, etc.) remain relevant, the scale of subscriber counts has grown exponentially."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f76442d6-d02e-4f26-b9d6-c3183e1d6929",
   "metadata": {},
   "source": [
    "## Pledge\n",
    "\n",
    "By submitting this work I hereby pledge that this is my own, personal work. I've acknowledged in the designated place at the top of this file all sources that I used to complete said work, including but not limited to: online resources, books, and electronic communications. I've noted all collaboration with fellow students and/or TA's. I did not copy or plagiarize another's work.\n",
    "\n",
    "> As a Boilermaker pursuing academic excellence, I pledge to be honest and true in all that I do. Accountable together – We are Purdue.\n",
    "\n",
    "https://www.purdue.edu/odos/osrr/honor-pledge/\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "seminar",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
