using System.Collections;
using System.IO;
using UnityEngine;
using UnityEngine.Networking;
using TMPro;

public class VoiceRecorder : MonoBehaviour
{
    public TextMeshProUGUI responseText;
    private AudioSource audioSource;
    private string backendUrl = "http://localhost:5000/predict";
    private string recordedFilePath;

    private AudioClip recordingClip;
    private bool isRecording = false;

    void Start()
    {
        audioSource = GetComponent<AudioSource>();
    }

    public void StartRecording()
    {
        if (isRecording) return;

        Debug.Log("Recording started...");
        responseText.text = "🎙️ Listening...";
        isRecording = true;
        recordingClip = Microphone.Start(null, false, 30, 44100);
    }

    public void StopRecording()
    {
        if (!isRecording) return;

        Microphone.End(null);
        isRecording = false;
        Debug.Log("Recording stopped.");

        byte[] wavData = WavUtility.FromAudioClip(recordingClip, out recordedFilePath);
        StartCoroutine(SendToBackend(wavData));
    }

    IEnumerator SendToBackend(byte[] wavData)
    {
        if (wavData == null)
        {
            Debug.LogError("WAV data is null.");
            yield break;
        }

        WWWForm form = new WWWForm();
        form.AddBinaryData("file", wavData, "recorded_audio.wav", "audio/wav");

        UnityWebRequest request = UnityWebRequest.Post(backendUrl, form);
        request.downloadHandler = new DownloadHandlerBuffer();

        yield return request.SendWebRequest();

        if (request.result != UnityWebRequest.Result.Success)
        {
            Debug.LogError("Error: " + request.error);
        }
        else if (request.responseCode == 200)
        {
            Debug.Log("Received audio from backend.");

            string audioSavePath = Path.Combine(Application.persistentDataPath, "response.wav");
            File.WriteAllBytes(audioSavePath, request.downloadHandler.data);

            StartCoroutine(PlayReceivedAudio(audioSavePath));
        }
        else
        {
            Debug.LogError("Error: " + request.downloadHandler.text);
        }
    }

    IEnumerator PlayReceivedAudio(string filePath)
    {
        using (UnityWebRequest www = UnityWebRequestMultimedia.GetAudioClip("file://" + filePath, AudioType.WAV))
        {
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError("Audio load error: " + www.error);
                yield break;
            }

            AudioClip clip = DownloadHandlerAudioClip.GetContent(www);
            audioSource.clip = clip;
            audioSource.Play();

            responseText.text = "Assistant: (Audio played)";
        }
    }
}
